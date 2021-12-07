module Main where

import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

type Input  = [Crab]
type Result = Fuel

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 7"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 = solve fuelcost
  where fuelcost = id

-- * Part 2

solve2 :: Input -> Result
solve2 = solve fuelcost
 where fuelcost distance = (distance * (distance + 1)) `div` 2

solve :: (Distance -> Fuel) -> [Crab] -> Fuel
solve fuelcost crabs = minimum $ map fuelCostTo [minimum crabs .. maximum crabs]
  where
    fuelCostTo :: Pos -> Fuel
    fuelCostTo = (sum . map fuelcost) . flip move crabs
    move :: Pos -> [Crab] -> [Distance]
    move destination = map (\crab -> abs $ crab - destination)

-- * Data Types

type Crab     = Int
type Fuel     = Int
type Pos      = Int
type Distance = Int

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = number `sepBy` char ','

number :: Parser Int
number = read <$> many digit
