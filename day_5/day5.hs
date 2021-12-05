module Day5 where

import           Control.Applicative hiding (many, (<|>))
import qualified Data.Map            as M
import           Data.Maybe          (mapMaybe)
import           Text.Parsec         hiding (Line, parse)
import           Text.Parsec.String

type Input  = [Line]
type Result = Int

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 5"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 lines = solve seafloor
  where seafloor = map (liftL trace) . filter straight $ lines

solve :: Seafloor -> Int
solve = M.size . M.filter (>= 2) . diagram . mapSeafloor

mapSeafloor :: Seafloor -> [Mapping]
mapSeafloor = map $ foldr (\c -> M.insert c 1) mempty

diagram :: [Mapping] -> Mapping
diagram = foldr (M.unionWith (+)) mempty

trace :: Coord -> Coord -> [Coord]
trace some other = [ C x y | x <- [x first .. x last], y <- [y first .. y last]]
  where first = minC some other
        last  = maxC some other

straight :: Line -> Bool
straight l = x1 l == x2 l || y1 l == y2 l

-- * Part 2

solve2 :: Input -> Result
solve2 lines = solve seafloor
  where straights = map (liftL trace) . filter straight $ lines
        diagonals = mapMaybe (liftL diagonal) $ lines
        seafloor  = straights <> diagonals

diagonal :: Coord -> Coord -> Maybe [Coord]
diagonal some other
  | abs (x last - x first) == abs (y last - y first) = pure $ zipWith C xs ys -- 45 degrees make the dream work
  | otherwise = Nothing
  where first  = minC some other
        last   = maxC some other
        xs = if x last < x first
             then [x last, x last + 1 .. x first] -- Form a right diagonal
             else [x last, x last - 1 .. x first] -- Form a left diagonal
        ys = [y last, y last - 1 .. 0]

-- * Data Types

type Seafloor = [[Coord]]

type Mapping  = M.Map Coord Int

data Coord = C { x :: Int
               , y :: Int
               }
  deriving (Eq, Ord)

data Line  = L { left  :: Coord
               , right :: Coord
               }
  deriving (Eq)

x1 = x . left
x2 = x . right
y1 = y . left
y2 = y . right

-- | Lift a function on Coordinates to a Line
liftL :: (Coord -> Coord -> a) -> (Line -> a)
liftL f line = f (left line) (right line)

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
  return (L left right)

coordinate :: Parser Coord
coordinate = do
  x <- number
  char ','
  y <- number
  return (C x y)

number :: Parser Int
number = read <$> many digit
