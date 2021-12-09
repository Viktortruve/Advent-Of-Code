module Main where

import qualified Data.Map as M
import           Data.Char (digitToInt)
import           Data.Tuple (swap)
import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 9"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 = sum . map risklevel . lowpoints
  where risklevel = succ

lowpoints :: Grid -> [Int]
lowpoints = map pluckLowest . filter hasLowestPoint . areas
  where
    hasLowestPoint (a, b, c, d, e) = c </ [a,b,d,e]
    pluckLowest (_,_,c,_,_) = c

areas :: Grid -> [Area]
areas grid = map mapArea coordinates
    where
      coordinates = M.keys grid
      mapArea (x, y) =
        (peek grid (x, y - 1), -- top
         peek grid (x - 1, y), -- left
         peek grid (x, y),     -- this point
         peek grid (x, y + 1), -- right
         peek grid (x + 1, y)) -- bottom

(</) :: Ord a => a -> [a] -> Bool
(</) x = not . any (<= x)

peek :: Grid -> Coord -> Int
peek = flip (M.findWithDefault wall)
  where
    wall = 10

-- * Part 2

solve2 :: Input -> Result
solve2 = undefined

-- * Data Types

type Input   = Grid
type Result  = Int

type Area = (Int, Int, Int, Int, Int)

type Coord = (Int, Int)
type Grid = M.Map Coord Int

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = do
  rows <- manyTill row eof
  pure $ M.fromList $
    concatMap (\(index, row) -> zip (zip (repeat index) [0 ..]) row) (zip [0 ..] rows)

row :: Parser [Int]
row = manyTill number space

number :: Parser Int
number = digitToInt <$> digit
