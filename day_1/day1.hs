module Day1 where

main :: IO ()
main = do
  input <- parse <$> readFile "input.txt"
  putStrLn "DAY 1"
  putStrLn $ "Solution 1: " ++ solve1 input
  putStrLn $ "Solution 2: " ++ solve2 input

type Input = [Int]
type Result = String

parse :: String -> Input
parse = map read . lines

solve1 :: Input -> Result
solve1 = show . solution
  where solution xs = let differences = zipWith (-) (tail xs) xs
                      in count (> 0) differences

solve2 :: Input -> Result
solve2 = show . solution
  where solution xs = let windows     = zip3 (tail (tail xs)) (tail xs) xs
                          sums        = map (\(a,b,c) -> a+b+c) windows
                          differences = zipWith (-) (tail sums) sums
                      in count (> 0) differences

count :: (a -> Bool) -> [a] -> Int
count p = length . filter p
