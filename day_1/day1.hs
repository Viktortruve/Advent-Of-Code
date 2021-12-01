module Day1 where

type Input = [Int]
type Result = Int

main :: IO ()
main = do
  input <- parse <$> readFile "input.1.txt"
  putStrLn "DAY 1"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

parse :: String -> Input
parse = map read . lines

solve1 :: Input -> Result
solve1 xs = length . filter (\(a, b) -> a > b) $ zip (tail xs) xs

solve2 :: Input -> Result
solve2 xs = solve1 $ zipWith3 (\a b c -> a + b + c) (tail (tail xs)) (tail xs) xs
