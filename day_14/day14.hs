module Main where

import Control.Monad.State
import qualified Data.MultiSet as MS
import qualified Data.Map.Strict as M
import           Text.Parsec        hiding (State, Line, parse, count)
import           Text.Parsec.String

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 13"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 = count . (flip execState mempty) . uncurry (fishAlgorithm 10)

-- * Part 2

solve2 :: Input -> Result
solve2 = count . (flip execState mempty) . uncurry (fishAlgorithm 40)

-- * Smarter solution, thanks day 6

fishAlgorithm :: Int -> Rules -> Template -> Counter Element (MS.MultiSet Pair)
fishAlgorithm 0 rules template = do
  let pairs = (zip template (tail template))
  put (MS.fromList template) -- Initial state
  pure (MS.fromList pairs)   -- Initial reactions
fishAlgorithm n rules template = do
  -- A set of pair, which each describe
  -- how many of each to put into the set
  -- which we propagate
  previousReaction <- fishAlgorithm (n - 1) rules template
  modify $ bumpElements previousReaction
  pure $ MS.foldOccur adjust previousReaction previousReaction
  where
    adjust element occurences set =
       let (left, right) = insertion rules element
       in   MS.insertMany right occurences
          . MS.insertMany left occurences
          . MS.deleteMany element occurences
          $ set

    bumpElements reactions previousElements = MS.union previousElements newElements
      where
        newElements = MS.fromOccurList $ map
          (\(pair, occurences) -> let Just element = M.lookup pair rules in (element, occurences))
          (MS.toOccurList reactions)

insertion :: Rules -> Pair -> (Pair, Pair)
insertion rules substance@(a, b) = ((a, element), (element, b))
  where
    Just element = M.lookup substance rules

count :: MS.MultiSet a -> MS.Occur
count counter = max - min
  where count = map snd . MS.toOccurList $ counter
        (max, min) = (maximum count, minimum count)

-- * Data Types

type Input = (Rules, Template)
type Result = Int

type Template  = [Char]
type Element   = Char
type Pair      = (Char, Char)
type Rules     = M.Map Pair Char
type Counter a = State (MS.MultiSet a)

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = do
  template <- many letter <* newline
  newline
  rules <- M.fromList <$> rulesp
  pure (rules, template)
  where
    rulesp = manyTill (rulep <* newline) eof

rulep :: Parser (Pair, Char)
rulep = do
  f <- letter
  s <- letter
  string " -> "
  element <- letter
  pure ((f, s), element)
