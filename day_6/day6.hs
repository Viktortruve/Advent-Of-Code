module Main where

import qualified Data.MultiSet as MS
import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

type Input  = [Int]
type Result = Int

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 6"
  putStrLn $ "Solution 1: " ++ show (solve input 80)
  putStrLn $ "Solution 2: " ++ show (solve input 256)

solve :: Input -> Int -> Result
solve input = sum' . day
  where
    sum'  = MS.foldOccur (\_ occurences res -> occurences + res) 0
    day 0 = MS.fromList input
    day d
      = MS.insertMany 8 spawns
      . MS.insertMany 6 spawns
      . MS.filter (>= 0)
      $ MS.map pred previousDay
      where
        previousDay = day (d - 1)
        spawns = MS.occur 0 previousDay


-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = number `sepBy` char ','

number :: Parser Int
number = read <$> many digit
