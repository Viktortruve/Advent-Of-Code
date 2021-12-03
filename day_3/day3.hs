module Day3 where

import Prelude hiding (not)
import Data.List (transpose, partition)

type Input  = [[Binary]]
type Result = Int

data Binary = Zero | One
  deriving (Eq)

not :: Binary -> Binary
not Zero = One
not One  = Zero

isone :: Binary -> Bool
isone One = True
isone _ = False

char2bin :: Char -> Binary
char2bin '1' = One
char2bin '0' = Zero

b2i :: [Binary] -> Int
b2i binary = sum [if isone bin then 2^power else 0 | (bin, power) <- xxx ]
  where xxx = zip (reverse binary) [0 ..]

main = do
  input <- parse <$> readFile "input.txt"
  putStrLn "DAY 3"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

parse :: String -> Input
parse = map (map char2bin) . lines

solve1 :: Input -> Result
solve1 i = powerconsumption
  where powerconsumption = b2i (gamma i) * b2i (epsilon i)

gamma :: Input -> [Binary]
gamma = map (common . partition isone) . transpose
  where
    common (ones, zeroes) = if length ones > length zeroes then One else Zero

epsilon :: Input -> [Binary]
epsilon = map not . gamma -- Invert the result of gamma to calculate least common bits

solve2 :: Input -> Result
solve2 = undefined
