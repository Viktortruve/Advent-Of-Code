module Main where

import Data.Foldable (asum)
import Data.Tuple (swap)
import qualified Data.Map as M
import Data.Maybe (mapMaybe)
import Data.List (sort, find, nub)
import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 8"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 input = sum $ map (count unique) $ map snd input
  where
    count p = length . filter p
    unique = not . M.null . obvi

-- * Part 2

solve2 :: Input -> Result
solve2 = sum . map ((read . concatMap show) . solveNote)

solveNote :: ([Signal], [Output]) -> [Number]
solveNote (signals, outputs) = decodedOutput
  where
    sortedSignals = map sort signals -- Normalize signals before doing any processing on them
    sortedOutputs = map sort outputs -- Outputs need to match up with normalizes signals

    decodedOutput :: [Number]
    decodedOutput = let mappings = decode sortedSignals
                    in mapMaybe (\output -> M.lookup output mappings) sortedOutputs

decode :: [Signal] -> M.Map Signal Number
decode signals = nonObvious <> obvious
  where
    obvious :: M.Map Signal Number
    obvious = decodeObvious signals

    nonObvious :: M.Map Signal Number
    nonObvious = case decodeNonObvious obvious signals of
                   Nothing -> error "Could not properly decode non obvious numbers .."
                   Just mappings -> mappings

decodeObvious :: [Signal] -> M.Map Signal Number
decodeObvious = foldr (M.union . obvi) mempty

obvi :: Signal -> M.Map Signal Number
obvi s
  | length s == 2 = M.singleton s One
  | length s == 4 = M.singleton s Four
  | length s == 3 = M.singleton s Seven
  | length s == 7 = M.singleton s Eight
  | otherwise = mempty

decodeNonObvious :: M.Map Signal Number -> [Signal] -> Maybe (M.Map Signal Number)
decodeNonObvious mappings signals
  | null unmappedSignals || null unmappedNumbers = pure mappings
  | otherwise =
  -- There are still unmapped letters to map, get going!
  -- Permuate all possible mappings of the remaining letters.
  -- Return a mapping of all the remaining letters such that there are no remaining unmapped letters.

  -- Pick the first mapping that completely solves the current note
  asum $ map (\mapping -> when makesSense (decodeNonObvious mapping signals)) possibleMappings
  where
    -- If the decoding is to work, then the remaining of the unmapped numbers has to have a mapping to all
    -- Signals.
    -- Thus, we start with the numbers instead.
    num = head unmappedNumbers
    possibleMappings = [ M.insert signal num mappings | signal <- unmappedSignals ] -- Among the signals that are left (sus), find a mapping from ONE signal onto `num`

    numbers  = [Zero .. Nine]
    mappedNumbers = M.elems mappings
    unmappedNumbers = filter (`notElem` mappedNumbers) numbers -- I.e. 3,5,6
    unmappedSignals = filter (\signal -> M.notMember signal mappings) signals

    when p ma = ma >>= \a -> if p a then pure a else mempty

-- | Check if a given mapping from signals to numbers make sense
makesSense :: M.Map Signal Number -> Bool
makesSense mappings =
  let correctLenghts = and $ zipWith (==) lenghts (sort $ map (\(num, signal) -> (num, length signal)) $ M.toList reverseMappings)
      validSegments = (length (five \/ two) == 3)                                -- 5,3 should all share 3 equal segments.
                      && (six \\ five == (eight \\ nine))                        -- identifies that a six is indeed a six
                      && (length (one \/ nine) == 2 && length (one \/ six) == 1) -- identifies that a nine is not a six
  in correctLenghts && validSegments
 where
   reverseMappings = invertMap mappings
   (Just one)      = M.lookup One reverseMappings
   (Just two)      = M.lookup Two reverseMappings
   (Just five)     = M.lookup Five reverseMappings
   (Just six)      = M.lookup Six reverseMappings
   (Just eight)    = M.lookup Eight reverseMappings
   (Just nine)     = M.lookup Nine reverseMappings
   lenghts = [(Zero, 6), (One, 2), (Two, 5), (Three, 5), (Four, 4), (Five, 5), (Six, 6), (Seven, 3), (Eight, 7), (Nine, 6)]

   invertMap :: (Ord k, Ord a) => M.Map k a -> M.Map a k
   invertMap = M.fromList . map swap . M.toList

-- | I.e. "abcdefg" `diff` "abcefg" == "d"
(\\) :: String -> String -> [Char]
(\\) s1 s2 = filter (`notElem` s2) s1

-- | I.e. "abc" `sim` "ab" == "ab"
(\/) :: String -> String -> [Char]
(\/) s1 s2 = filter (`elem` s2) s1

-- * Data Types

data Number = Zero | One | Two | Three | Four | Five | Six | Seven | Eight | Nine
  deriving (Eq, Ord, Enum)

instance Show Number where
  show Zero  = "0"
  show One   = "1"
  show Two   = "2"
  show Three = "3"
  show Four  = "4"
  show Five  = "5"
  show Six   = "6"
  show Seven = "7"
  show Eight = "8"
  show Nine  = "9"

type Signal  = [Char]
type Output  = [Char]
type Input   = [([Signal], [Output])]
type Result  = Int

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = parseNote `manyTill` eof

parseNote :: Parser ([Signal], [Output])
parseNote = do
  signals <- count 10 (segment <* char ' ')
  char '|'
  char ' '
  output <- count 4 (segment <* (char ' ' <|> char '\n'))
  pure (signals, output)

segment :: Parser [Char]
segment = many letter
