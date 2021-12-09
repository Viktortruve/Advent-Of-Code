module Main where

import qualified Data.Map as M
import           Data.Char (digitToInt)
import           Data.List (sort, nub)
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
solve1 grid = sum . map (risklevel . peek grid) . lowpoints $ grid
  where risklevel = succ

peek :: Grid -> Coord -> Int
peek = flip (M.findWithDefault wall)
  where
    wall = 10

lowpoints :: Grid -> [Coord]
lowpoints grid = map head . filter (hasLowestPoint . map (peek grid)) $ areas grid
  where
    hasLowestPoint points = head points </ tail points
    (</) :: Ord a => a -> [a] -> Bool
    (</) x = not . any (<= x)

areas :: Grid -> [[Coord]]
areas grid = map (\c -> c : neighbours grid c) coordinates
    where
      coordinates = M.keys grid

neighbours :: Grid -> Coord -> [Coord]
neighbours grid = filter valid . adjacents
  where
    valid :: Coord -> Bool
    valid = (<= 9) . peek grid
    adjacents (x, y) = [(x, y - 1), -- top
                        (x - 1, y), -- left
                        (x, y + 1), -- right
                        (x + 1, y)] -- bottom

-- * Part 2

solve2 :: Input -> Result
solve2 = product . take 3 . reverse . sort . map length . basins

basins :: Grid -> [Basin]
basins grid = map (explore grid) (lowpoints grid)

explore :: Grid -> Coord -> Basin
explore grid lowpoint = nub $ concatMap go (lowpoint : neighbours grid lowpoint)
  where
    hasNext origin next = next `notElem` [9, 10] && next > origin
    -- | Go in one direction, and return the trace of where we went
    go :: Coord -> [Coord]
    go c
      | val `elem` [9, 10]    = mempty
      | otherwise = let nabos = filter (hasNext val . peek grid) . neighbours grid $ c
                    in c : concatMap go nabos
      where val = peek grid c

-- * Data Types

type Input   = Grid
type Result  = Int

type Coord = (Int, Int)
type Basin = [Coord]
type Grid = M.Map Coord Int

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = do
  rows <- manyTill row eof
  -- Pair up each value with a coordinate
  pure $ M.fromList $
   concat [[ ((ri, ci), val) | (val, ci) <- indexed row] | (row, ri) <- indexed rows]
  where
    indexed xs = zip xs [0 ..]

row :: Parser [Int]
row = manyTill number space

number :: Parser Int
number = digitToInt <$> digit
