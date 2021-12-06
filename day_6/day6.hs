module Main where

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
solve input = sum . day
  where
    day 0 = let respawnTimers = [0..8]
                tillSpawn days = filter (== days) input
            in map (length . tillSpawn) respawnTimers -- How many fishes are there for each spawn timer?

    day d = let (spawn:otherdays) = day (d - 1)
            in zipWith (+) (otherdays ++ [0])      -- since 'day 0' fishes are popped off the list of days, we have to insert a 0 at the end of the list
               [0, 0, 0, 0, 0, 0, spawn, 0, spawn] -- Those fishes that are on day 0 are moved to position 6, and leave a spawn at position 8

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = number `sepBy` char ','

number :: Parser Int
number = read <$> many digit
