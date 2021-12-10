module Main where

import           Data.List     (sort)
import           Data.Either   (partitionEithers)
import           Data.Foldable (foldlM)

main :: IO ()
main = do
  (corrupt, incomplete) <- partitionEithers . map stack . lines <$> readFile "input.txt"
  putStrLn "DAY 10"
  putStrLn $ "Solution 1: " ++ show (solve1 corrupt)
  putStrLn $ "Solution 2: " ++ show (solve2 incomplete)

-- * Part 1

solve1 :: [Char] -> Result
solve1 = sum . map score
  where score ')' = 3
        score ']' = 57
        score '}' = 1197
        score '>' = 25137

-- * Part 2

solve2 :: [[Char]] -> Result
solve2 = middle . sort . map (calcscore . autocomplete)
  where score ')' = 1
        score ']' = 2
        score '}' = 3
        score '>' = 4
        calcscore = foldr (\b tot -> tot * 5 + score b) 0
        autocomplete = map inverse . reverse
        middle as = as !! (length as `div` 2)

-- * Data Types

type Result = Int

stack :: String -> Either Char [Char]
stack = foldlM go []
  where go stack b
          | open b = pure $ b : stack
          | otherwise =
            case stack of
              [] -> pure [b]
              (top:rest) -> if top == inverse b then pure rest else Left b

inverse :: Char -> Char
inverse '(' = ')'
inverse '[' = ']'
inverse '{' = '}'
inverse '<' = '>'
inverse ')' = '('
inverse ']' = '['
inverse '}' = '{'
inverse '>' = '<'

open :: Char -> Bool
open = (`elem` ['(', '[', '{', '<'])
