module Main where

import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

type Input  = Crabs
type Result = Fuel

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 7"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 input = let possiblePositions = [min' .. max']
               in  minimum $ map (move input) possiblePositions
  where max' = maximum input
        min' = minimum input
        move :: Crabs -> Int -> Fuel
        move crabs destination = sum $ map (\crab -> abs $ crab - destination) crabs

-- * Part 2

solve2 :: Input -> Result
solve2 input = let possiblePositions = [min' .. max']
               in  minimum $ map (move input) possiblePositions
  where max' = maximum input
        min' = minimum input
        move :: Crabs -> Int -> Fuel
        move crabs destination = sum $ map (\crab -> fuelcost $ abs (crab - destination)) crabs
        fuelcost n = (n * (n + 1)) `div` 2

-- * Data Types

type Crabs = [Int]
type Fuel  = Int

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = number `sepBy` char ','

number :: Parser Int
number = read <$> many digit
