module Day4 where

import           Control.Applicative hiding (many, (<|>))
import           Data.List           (find, transpose)
import           Prelude             hiding (round)
import           Text.Parsec         hiding (parse)
import           Text.Parsec.String

type Input  = ([Int], [Board])
type Result = Int

type Board = [Row]
type Row   = [Tile]
data Tile = T { num    :: Int
              , marked :: Bool
              }

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 4"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

solve :: (Board -> Bool) -> Int -> [Board] -> Result
solve chickendinner draw boards = case find chickendinner boards of
                                   Just board -> score draw board
                                   Nothing    -> undefined

solve1 :: Input -> Result
solve1 (draws, boards) = solve winner d bs
  where
    (d, bs) = head $ dropWhile (not . any winner . snd) (play draws boards)

solve2 :: Input -> Result
solve2 (draws, boards) = solve ((not . winner) . unmark d) d bs
  where rounds        = play draws boards
        winningBoards = length . filter winner . snd . last $ rounds
        (d, bs)       = last . takeWhile ((== winningBoards) . length . filter winner . snd) . reverse $ rounds

winner :: Board -> Bool
winner board = any (all marked) board || any (all marked) (transpose board)

play :: [Int] -> [Board] -> [(Int, [Board])]
play ds boards = scanl round (head ds, boards) ds

round :: (Int, [Board]) -> Int -> (Int, [Board])
round (_, boards) draw = (draw, map (mark draw) boards)

score :: Int -> Board -> Result
score last = (last *) . sum . map num . filter (not . marked) . concat

mark :: Int -> Board -> Board
mark n = map (map (markT n True))

unmark :: Int -> Board -> Board
unmark n = map (map (markT n False))

markT :: Int -> Bool -> Tile -> Tile
markT n b t = if num t == n then t { marked = b } else t

-- * Today's parsing was fun and enjoyable. :-)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = do
  d  <- draws
  many newline
  bs <- manyTill (board <* many newline) eof
  pure (d, bs)

board :: Parser Board
board = mkBoard <$> count 5 row
  where mkBoard = map (map (`T` False))

row :: Parser [Int]
row = (whitenoise *> number <* whitenoise) `manyTill` newline
      where whitenoise = many (char ' ')

draws :: Parser [Int]
draws = number `sepBy` char ','

number :: Parser Int
number = read <$> many digit
