module Day3 where

import Prelude hiding (not)
import Data.List (transpose, partition)

type Input  = [[Binary]]
type Result = Int

data Binary = Zero | One
  deriving (Eq, Show)

not :: Binary -> Binary
not Zero = One
not One  = Zero

isone :: Binary -> Bool
isone One = True
isone _ = False

char2bin :: Char -> Binary
char2bin '1' = One
char2bin '0' = Zero
char2bin _ = undefined

b2i :: [Binary] -> Int
b2i binary = sum [if isone bit then 2^power else 0 | (bit, power) <- bits ]
  where bits = zip (reverse binary) [0 ..]

main = do
  input <- parse <$> readFile "input.txt"
  putStrLn "DAY 3"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

parse :: String -> Input
parse = map (map char2bin) . lines

solve1 :: Input -> Result
solve1 i = gammarating * epsilonrating
  where gammarating   = b2i . gamma $ i
        epsilonrating = b2i . epsilon $ i

gamma :: Input -> [Binary]
gamma = map (mostCommon None . partition isone) . transpose

epsilon :: Input -> [Binary]
epsilon = map not . gamma -- Invert the result of gamma to calculate least common bits

solve2 :: Input -> Result
solve2 i = co2 * ogr
  where
    co2 = b2i . findObscureRating CO2 $ i
    ogr = b2i . findObscureRating OGR $ i

data Criteria = CO2 | OGR | None
  deriving (Eq, Show)

findObscureRating  :: Criteria -> Input -> [Binary]
findObscureRating criteria input = pluckRating $ scanl (flip (criteriafilter criteria)) input positions
  where
    pluckRating = head . head . dropWhile ((> 1) . length)
    positions = [0..(length input)]

criteriafilter :: Criteria -> Int -> [[Binary]] -> [[Binary]]
criteriafilter c pos input = filter hasMostCommonBit input
  where mostCommonBit    = mostCommon c . partition isone . map (!! pos)
        keep             = mostCommonBit input
        hasMostCommonBit = \num -> (num !! pos) == keep

mostCommon :: Criteria -> ([Binary], [Binary]) -> Binary
mostCommon None (ones, zeroes)
  | length ones > length zeroes = One
  | otherwise = Zero
mostCommon CO2 (ones, zeroes)
  | length ones == length zeroes = Zero
  | length zeroes < length ones  = Zero
  | otherwise = One
mostCommon OGR input = not . mostCommon CO2 $ input
