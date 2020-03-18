# Hangman_game
ENGS 110 individual project

Target audience - People who want to spend their leisure time plating an intelectual game

In the game, one guesses a word in limited amount of trials
Initially, some amount of words(sorted in different categories) are stored.
Useg picks a category, then the programm randomly chooses a word from that category.
Uses guesses letters, if the word has that letter, program shows it (E.g. hidden word is "glasses", the guessed letter is "s" then the console will show ***ss*s). If the used fails to guess the word after some trials, game ends
Also, after 2-3 failed guesses, one can take a hint

Data to store in json
username: player inputs his username which gets stored in json file
under player's username there will be stored:
Words he guessed with the number of guesses he used to guess the word. 
also, categories will be saved with the information, whether hint was used or not. Perhaps, the concept of point will be added.
    or, if the game has the opportunity to end after some failed guesses, player's successful and not successful trials
 
