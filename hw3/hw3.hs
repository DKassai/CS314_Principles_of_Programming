skips :: [a] -> [[a]]
skips xs = [ [ word | (i, word) <-zip[1..] xs, mod i k == 0] | k <- [1..length xs]] 


localMaxima :: [Integer] -> [Integer]
localMaxima [] = []
localMaxima (a : []) = []
localMaxima (a:b:[]) = []
localMaxima (a:b:c:zs) = if b > a && b > c 
			then b: localMaxima (b:c:zs) 
			else localMaxima (b:c:zs)


freq xs = map (\n -> length (filter (== n) xs)) [0..9]

history xs y = map (\x -> if x < y then ' ' else '*') xs

histogram :: [Integer] -> String
histogram xs = m ++ "==========\n" ++ "0123456789\n"
    where largest = freq xs
          len = maximum largest
          m = unlines (map (history largest) [len, len-1..1])
