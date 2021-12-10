module Main where

import           Data.List     (sort)
import           Data.Either   (rights, lefts)
import           Data.Foldable (foldlM)
import           Text.Parsec        hiding (Line, parse)
import           Text.Parsec.String

main :: IO ()
main = do
  input <- parse "input.txt"
  putStrLn "DAY 10"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

-- * Part 1

solve1 :: Input -> Result
solve1 = sum . map score . lefts . map mkStack
  where
    score :: StackError -> Int
    score (IllegalBrace b) =
      case b of
        (L, _) -> 0
        (R, p) -> case p of
          Soft  -> 3
          Hard  -> 57
          Curly -> 1197
          Angle -> 25137
    score _ = 0

mkStack :: Line -> Either StackError (Stack Brace)
mkStack = foldlM iter []
  where iter :: Stack Brace -> Brace -> Either StackError (Stack Brace)
        iter stack b =
          case b of
            (L, _) -> pure $ push stack b -- Put it on the pile
            (R, _) -> do
              case peek stack of
                Nothing -> pure $ push stack b
                Just top -> do -- There is some brace at the top
                  if top == inverse b -- I.e. top: '(', b: ')' => '(' == inverse ')': True
                    then pop' stack
                    else Left $ IllegalBrace b -- Top character does not match incomming inverse. As such, we have failed as parents.

-- * Part 2

solve2 :: Input -> Result
solve2 = middle . sort . map (calcScore . autocomplete) . rights . map mkStack
  where
    score Soft  = 1
    score Hard  = 2
    score Curly = 3
    score Angle = 4
    calcScore = foldl (\tot b -> tot * 5 + score (snd b)) 0

autocomplete :: Stack Brace -> [Brace]
autocomplete = reverse . map inverse . reverse

middle :: [a] -> a
middle as = as !! (length as `div` 2)

-- * Data Types

type Input   = [Line]
type Result  = Int

type Line = [Brace]

type Brace = (Dir, Paren)

data Paren
  = Soft
  | Hard
  | Curly
  | Angle
  deriving (Show, Eq)

data Dir = L | R
  deriving (Show, Eq)

type Stack a = [a]

data StackError
  = EmptyStack
  | IllegalBrace Brace
  deriving Show

pop' :: Stack a -> Either StackError (Stack a)
pop' s = do
  (top, rest) <- pop s
  pure rest

pop :: Stack a -> Either StackError (a, Stack a)
pop []     = Left EmptyStack
pop (x:xs) = pure (x, xs)

peek :: Stack a -> Maybe a
peek []     = Nothing
peek (x:xs) = pure x

push :: Stack a -> a -> Stack a
push xs x = x : xs

inverse :: Brace -> Brace
inverse (R, p) = (L, p)
inverse (L, p) = (R, p)

-- * Today's parsing was actually fun and enjoyable. (no sarcasm)

parse :: FilePath -> IO Input
parse input = either (error . show) id <$> parseFromFile parser input

parser :: Parser Input
parser = manyTill line eof

line :: Parser [Brace]
line = manyTill brace (char '\n')

brace :: Parser Brace
brace = soft <|> hard <|> curly <|> angle

soft :: Parser Brace
soft = mkBrace Soft '(' ')'

hard :: Parser Brace
hard = mkBrace Hard '[' ']'

curly :: Parser Brace
curly = mkBrace Curly '{' '}'

angle :: Parser Brace
angle = mkBrace Angle '<' '>'

mkBrace :: Paren -> Char -> Char -> Parser Brace
mkBrace b l r = do
  d <- (char l *> pure L) <|> (char r *> pure R)
  pure (d, b)
