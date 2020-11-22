# Hangman_game
ENGS 110 individual project

Target audience - People who want to spend their leisure time plating an intelectual game

In the game, one guesses a word that was picked randomly by the computer under a particular category, picked by the player
Initially, some amount of words(sorted in different categories) are stored.
Useg picks a category, then the programm randomly chooses a word from that category.
Uses guesses letters, if the word has that letter, program shows it (E.g. hidden word is "glasses", the guessed letter is "s" then the console will show ***ss*s). If the used fails to guess the word after some trials, game ends
Also, after 2-3 failed guesses, one can take a hint

Data to store in json
username: player inputs his username which gets stored in json file
under player's username there will be stored:
points: number of points that the user gains or loses during the game
Words he guessed with the number of guesses he used to guess the word. 
The favorite category of the user
words guesses: shows all the words a user has ever guessed
categories picked: shoes all categories the user has ever picked

After guessing the word, the user will have an opportunity to see his or her statistics that will show the information stored in a json file
 
