module Day5 where

import qualified Data.Map           as M
import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

type Input  = [Line]
type Result = Int

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 5"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

solve :: Seafloor -> Int
solve = M.size . M.filter (>= 2) . seafloor

-- * Part 1

solve1 :: Input -> Result
solve1 = solve . foldMap straight

straight :: Line -> Seafloor
straight (some, other)
  | x some == x other || y some == y other = s [ C x y | x <- [x first .. x last], y <- [y first .. y last]]
  | otherwise = mempty
  where first = minC some other
        last  = maxC some other

-- * Part 2

solve2 :: Input -> Result
solve2 lines = solve (straights <> diagonals)
  where straights = foldMap straight lines
        diagonals = foldMap diagonal lines

diagonal :: Line -> Seafloor
diagonal (some, other)
  | abs (x last - x first) == abs (y last - y first) = s (zipWith C xs ys) -- 45 degrees make the dream work
  | otherwise = mempty
  where first = minC some other
        last  = maxC some other
        xs = x last ... x first
        ys = [y last, y last - 1 .. 0]

(...) :: Int -> Int -> [Int]
(...) x y
  | x < y     = [x, x + 1 .. y] -- Form a right diagonal
  | otherwise = [x, x - 1 .. y] -- Form a left diagonal

-- * Data Types

newtype Seafloor = S { seafloor :: M.Map Coord Int }

s :: [Coord] -> Seafloor
s = S . M.fromList . map (\c -> (c, 1))

instance Semigroup Seafloor where
  (S some) <> (S other) = S (M.unionWith (+) some other)

instance Monoid Seafloor where
  mempty = S M.empty

type Line  = (Coord, Coord)

data Coord = C { x :: Int
               , y :: Int
               }
  deriving (Eq, Ord)

maxC :: Coord -> Coord -> Coord
maxC c1 c2
  | y c1 > y c2  = c1
  | y c1 == y c2 = if x c1 > x c2 then c1 else c2
  | otherwise    = c2

minC :: Coord -> Coord -> Coord
minC c1 c2 = if maxC c1 c2 /= c1 then c1 else c2

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = (line <* many newline) `manyTill ` eof

line :: Parser Line
line = do
  left  <- coordinate
  string " -> "
  right <- coordinate
  return (left, right)

coordinate :: Parser Coord
coordinate = do
  x <- number
  char ','
  y <- number
  return (C x y)

number :: Parser Int
number = read <$> many digit
