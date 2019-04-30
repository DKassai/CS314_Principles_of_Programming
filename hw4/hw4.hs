import System.Random
import System.IO
import Data.Sequence
import Data.Foldable
import Data.Char

helper_file = ".hw4.svg"

get_the_underscores xs = map (\x -> '_') xs

increment :: String -> Char -> [Int]
increment xs x = get_the_index xs x 0

get_the_index :: String -> Char -> Int -> [Int]
get_the_index [] x i = []
get_the_index xs x i = if (head xs) == x
	    then i : get_the_index (tail xs) x (i+1)
	    else get_the_index (tail xs) x (i+1)

replace_letter :: String -> Char -> [Int] -> String
replace_letter xs c i = replace_a_single_char xs c i 0

replace_a_single_char :: String -> Char -> [Int] -> Int -> String
replace_a_single_char [] _ _ _ = []
replace_a_single_char (j:xsT) c i x = if Data.Foldable.elem x i
    then c : replace_a_single_char xsT c i (x+1)
    else j : replace_a_single_char xsT c i (x+1)

main :: IO()
main = do
    readf <- openFile "words.txt" ReadMode
    word_String <- (readFile "words.txt")

    let list_of_words = lines word_String
    hClose readf
    i <- randomRIO(0, Prelude.length list_of_words)
    let game_word = list_of_words !! i
    let raw_board = get_the_underscores game_word


    writeFile helper_file raw_board
    let game_loop = do

        game_board <- (readFile helper_file)
        if Data.Foldable.elem '_' game_board
        then do
            putStrLn game_board
            raw_input <- getChar
            let player_input = toLower raw_input
            putStrLn ""
            let index_address = (increment (game_word) (player_input))

            if index_address /= []
                then do
                    let board2 = replace_letter game_board player_input index_address
                    writeFile helper_file board2
                    putStr ""
                else putStrLn "Letter is not in the word. Please select another letter"

            game_loop
	else do
            putStrLn game_board
            putStrLn "You won the game!!"
    game_loop

