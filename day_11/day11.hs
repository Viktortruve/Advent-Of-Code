module Main where

import qualified Data.Map as M
import           Data.Char (digitToInt)
import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 11"
  --print input
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 grid = snd $ (!! 100) $ iterate step (grid, 0)

step :: (Grid, Int) -> (Grid, Int)
step (g, n) = let g' = spread . initial $ g
              in (cooldown g', n + flashes g')

initial :: Grid -> Grid
initial = M.map (fmap succ)

cooldown :: Grid -> Grid
cooldown = M.map x
  where
    x Fizzled = Charging 0
    x y = y

flashes :: Grid -> Int
flashes = sum . M.map flashed
  where
    flashed Fizzled = 1
    flashed _ = 0

-- | Mark every octopus with a charge level over 9 as flashed
mark :: Grid -> Grid
mark = M.map x
  where
    x (Charging l)
      | l > 9 = Flashing
      | otherwise = Charging l
    x y = y

spread :: Grid -> Grid
spread grid
  | M.null (M.filter flashing g') = grid
  | otherwise = let nabos = concatMap neighbours . getFlashing $ g'
                in spread . fizzle $ foldl (\g'' -> inject g'' (fmap succ)) g' nabos
  where
    g' = mark grid


fizzle :: Grid -> Grid
fizzle g = foldl (`inject` fizzleout) g (M.keys g)
  where
    fizzleout Flashing = Fizzled
    fizzleout x = x

flashing :: Status a -> Bool
flashing Flashing = True
flashing _ = False

getFlashing :: Grid -> [Coord]
getFlashing = M.keys . M.filter flashing

inject :: Grid -> (Counter -> Counter) -> Coord -> Grid
inject grid f c = M.adjust f c grid

neighbours :: Coord -> [Coord]
neighbours (x, y) =
  [(x + r, y + c) | (r, c) <- [ (-1, -1) , (-1, 0), (-1, 1)
                              , (0, -1), (0, 1)
                              , (1, -1), (1, 0), (1, 1)]]

-- * Part 2

solve2 :: Input -> Result
solve2 grid =
  succ
  . length
  . takeWhile (\((_, s'), (_, s)) -> s' - s /= diff)
  $ zip (tail sim) sim
  where
    sim = iterate step (grid, 0)
    diff = 10 * 10

-- * Data Types

type Result = Int
type Input  = Grid

data Status a
  = Flashing
  | Fizzled
  | Charging a
  deriving Show

instance Functor Status where
  fmap f Fizzled = Fizzled
  fmap f Flashing = Flashing
  fmap f (Charging a) = Charging $ f a

type Counter = Status Int
type Coord = (Int, Int)
type Grid = M.Map Coord Counter

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = do
  rows <- manyTill row eof
  -- Pair up each value with a coordinate
  pure $ M.fromList $
   [ ((ri, ci), Charging val)
   | (row, ri) <- indexed rows
   , (val, ci) <- indexed row
   ]
  where
    indexed xs = zip xs [0 ..]

row :: Parser [Int]
row = manyTill number space

number :: Parser Int
number = digitToInt <$> digit
