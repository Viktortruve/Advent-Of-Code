module Day2 where

type Input = [Move]
type Result = Int

data Position = MkPos { horizontal :: Int
                      , depth      :: Int
                      , aim        :: Int
                      }

data Move = Up Int | Down Int | Forward Int

main :: IO ()
main = do
  input <- parse <$> readFile "input.txt"
  putStrLn "DAY 2"
  putStrLn $ "Solution 1: " ++ show (solve1 input)
  putStrLn $ "Solution 2: " ++ show (solve2 input)

parse :: String -> Input
parse i = map parseMove $ lines i
  where parseMove :: String -> Move
        parseMove = (\(m:v:_) -> mkMove m (read v)) . words
        mkMove :: String -> Int -> Move
        mkMove "up"      = Up
        mkMove "down"    = Down
        mkMove "forward" = Forward

solve1 :: Input -> Result
solve1 =  (\p -> horizontal p * depth p) . foldl (flip move) (MkPos { horizontal = 0, depth = 0 })
  where
    updateDepth f p      = p { depth = f (depth p) }
    updateHorizontal f p = p { horizontal = f (horizontal p) }
    move :: Move -> Position -> Position
    move (Up d)      = updateDepth (\x -> x - d)
    move (Down d)    = updateDepth (+ d)
    move (Forward h) = updateHorizontal (+ h)

solve2 :: Input -> Result
solve2 = (\p -> horizontal p * depth p) . foldl (flip move) (MkPos { horizontal = 0, depth = 0, aim = 0 })
  where
    updateDepth f p      = p { depth = f (depth p) (aim p) }
    updateHorizontal f p = p { horizontal = f (horizontal p) }
    updateAim f p        = p { aim = f (aim p) }
    move :: Move -> Position -> Position
    move (Up x)      = updateAim (+ x)
    move (Down x)    = updateAim (\a -> a - x)
    move (Forward x) = updateDepth (\d a -> d - a * x) . updateHorizontal (+ x)
