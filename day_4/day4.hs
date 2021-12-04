module Day4 where

import           Control.Applicative hiding (many, (<|>))
import           Data.Bifunctor      (bimap, second)
import           Data.List           (transpose)
import           Prelude             hiding (round)
import           Text.Parsec         hiding (parse)
import           Text.Parsec.String

type Input  = ([Int], [Board])
type Result = Int

type Board = [Row]
type Row   = [Tile]
data Tile  = T { num    :: Int
               , marked :: Bool
               }

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 4"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

solve1 :: Input -> Result
solve1 (draws, boards) = score draw board
  where
    winningRound = head . dropWhile (not . any winner . snd) $ play draws boards
    (draw, board) = second (head . filter winner) winningRound

solve2 :: Input -> Result
solve2 (draws, boards) = score draw board
  where
    (playedRounds, unplayedRounds) = break (all winner . snd) $ play draws boards
    (draw, board) = bimap
      (fst . head)
      (mark draw . head . filter (not . winner) . snd . last)
      (unplayedRounds, playedRounds)

score :: Int -> Board -> Result
score last = (last *) . sum . map num . filter (not . marked) . concat

play :: [Int] -> [Board] -> [(Int, [Board])]
play draws boards = scanl round (head draws, boards) draws
  where round (_, boards) draw = (draw, map (mark draw) boards)

winner :: Board -> Bool
winner board = bingo board || bingo (transpose board)
  where bingo = any (\row -> all marked row)

mark :: Int -> Board -> Board
mark n = map (map (\t -> if num t == n then t { marked = True } else t))

-- * Today's parsing was fun and enjoyable. :-)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = do
  d  <- draws
  many newline
  bs <- (board <* many newline) `manyTill ` eof
  pure (d, bs)

board :: Parser Board
board = count 5 row

row :: Parser Row
row = tile `manyTill` newline

tile :: Parser Tile
tile = do
  many (char ' ')
  n <- number
  pure $ T n False

draws :: Parser [Int]
draws = number `sepBy` char ','

number :: Parser Int
number = read <$> many digit
