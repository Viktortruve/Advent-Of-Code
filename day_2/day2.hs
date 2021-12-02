module Day2 where
data Position = MkPos { horizontal :: Int , depth :: Int , aim :: Int}
data Move = Up Int | Down Int | Forward Int
main = do input <- parse <$> readFile "input.txt"; putStrLn "DAY 2"; putStrLn $ "Solution 1: " ++ show (solve1 input); putStrLn $ "Solution 2: " ++ show (solve2 input)
parse = let mkMove "up" = Up ; mkMove "down" = Down ; mkMove "forward" = Forward ; in map ((\(m:v:_) -> mkMove m (read v)) . words) . lines
solve1 = let move (Up d) = \p -> p { depth = depth p - d } ; move (Down d) = \p -> p { depth = depth p + d } ; move (Forward h) = \p -> p { horizontal = horizontal p + h } ; in (\p -> horizontal p * depth p) . foldl (flip move) (MkPos { horizontal = 0, depth = 0, aim = 0 })
solve2 = let move (Up x) = \p -> p { aim = aim p + x }; move (Down x) = \p -> p { aim = aim p - x }; move (Forward x) = (\p -> p { depth = depth p - aim p * x}) . (\p -> p { horizontal = horizontal p + x}) in (\p -> horizontal p * depth p) . foldl (flip move) (MkPos { horizontal = 0, depth = 0, aim = 0 })
