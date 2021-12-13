module Main where

import Prelude hiding (break, flip)
import qualified Data.Map as M
import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 13"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn "Solution 2:"
  print (solve2 input)

-- * Part 1

solve1 :: Input -> Int
solve1 (instrs, sheet) = length . M.elems . unsheet $ fold (head instrs) sheet

foldMany :: [Instruction] -> Sheet -> Sheet
foldMany instrs sheet = foldl (\s i -> fold i s) sheet instrs

-- Left associative / Upper half associative. I.e. fold bottom half UP, fold right half LEFT
fold :: Instruction -> Sheet -> Sheet
fold i s = let (s1, s2) = break i s
           in s1 <> flip i s2

break :: Instruction -> Sheet -> (Sheet, Sheet)
break instr s =
  let (left, right) = M.partitionWithKey partitioner (unsheet s)
  in (S left, S $ M.mapKeys remapper right)
  where
    partitioner (x, y) _ =
      case instr of
        Horizontal line -> y < line
        Vertical   line -> x < line
    remapper (x, y) =
      case instr of
        Horizontal line -> (x, y - 1 - line)
        Vertical   line -> (x - 1 - line , y)

flip :: Instruction -> Sheet -> Sheet
flip line s = S $ M.mapKeys normalize (unsheet s)
  where
    normalize (x, y) =
      case line of
        Horizontal h -> if even h then (x, h - 1 - y) else (x, y `over` (h `div` 2))
        Vertical   v -> if even v then (v - 1 - x , y) else (x `over` (v `div` 2), y)

-- |'Rotate' a number over a point
over :: Int -> Int -> Int
over n p = let distance = n - p
           in n - distance * 2

-- * Part 2

solve2 :: Input -> Sheet
solve2 = uncurry foldMany

-- * Data Types

type Input = ([Instruction], Sheet)

data Instruction = Vertical Int | Horizontal Int -- Different types of folds
  deriving Show

-- A Sheet is a semigroup !
newtype Sheet = S { unsheet :: M.Map (Int, Int) Bool }

instance Semigroup Sheet where
  (S s1) <> (S s2) = S $ M.unionWith (\a b -> b) s1 s2

instance Show Sheet where
  show (S s) =
    unlines $ chunksOf (maxX + 1)
    [if peek (x, y) then '█' else ' ' | y <- [0 .. maxY], x <- [0.. maxX]]
    where
      dots = M.keys s
      maxX = maximum $ map fst dots
      maxY = maximum $ map snd dots

      peek k = M.findWithDefault False k s
      chunksOf n xs
        | n > length xs = pure xs
        | otherwise = take n xs : chunksOf n (drop n xs)

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = do
  marks <- dots
  newline
  instrs <- instructions
  pure (instrs, mkSheet marks)
  where
    dots = many (parseDot <* newline)
    instructions = manyTill (parseInstruction <* newline) eof
    mkSheet marks = S $ M.fromList (zip marks (repeat True))

parseDot :: Parser (Int, Int)
parseDot = do
  x <- number
  char ','
  y <- number
  pure (x, y)

parseInstruction :: Parser Instruction
parseInstruction = string "fold along " *> (x <|> y)
  where
    x = Vertical   <$> (string "x=" *> number)
    y = Horizontal <$> (string "y=" *> number)

number :: Parser Int
number = read <$> many digit
