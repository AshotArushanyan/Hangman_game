import random
import json
from single_linked_list import SingleLinkedList


class Json:

    with open('Hangman.json') as json_file:
        game = json.load(json_file)

    def __init__(self, list_of_categories, list_of_players, username, category, word, points):
        self.list_of_categories = list_of_categories
        self.list_of_players = list_of_players
        self.username = username
        self.category = category
        self.word = word
        self.points = points
        self.rank = ""

    def json_dump(self):
        with open('Hangman.json', 'w') as outfile:
            json.dump(Json.game, outfile, indent=2)

    def username_picking(self):
        self.username = input("please enter your username: ")
        print()
        if self.username not in self.list_of_players:
            self.list_of_players[self.username] = {"points": 50, "favorite_category": "",  "categories_picked": []}
        self.points = self.list_of_players[self.username]["points"]

    def category_picking(self):
        print(f'''Hello {self.username}, lets play a game. To start, you need to pick a category.''', end="\n\n")
        ll = SingleLinkedList()
        for i in self.game['categories'].keys():
            ll.insert_last(i)
        ll.print_list()
        print()
        self.category = input("Please pick a category: ")
        print()
        while True:
            if ll.find(self.category) is None:
                self.category = input("There is no such category. Please pick again: ")
                print()
            else:
                word_ll = SingleLinkedList()
                for i in self.list_of_categories[self.category]:
                    word_ll.insert_last(i)
                self.word = word_ll.pick_random()
                self.list_of_players[self.username]["categories_picked"].append(self.category.lower())
                self.list_of_players[self.username]["favorite_category"] = max(set(self.list_of_players[self.username]["categories_picked"]), key=self.list_of_players[self.username]["categories_picked"].count)
                break

    def defining_rules(self):
        print(f"""For each guessed letter you will earn 5 points.
For each failed guess you will lose 3 points.
For a taken hint you will lose 10 points.
IF you guess the word with no failed guesses, you additionaly get 20 points.
Good luck, now you have {self.points} points!""", end="\n\n")
        print(f"Now i think of a word under the category {self.category}. It is {len(self.word)} characters long. ", end="\n\n")

    def information_getting(self):
        info = input("If you want to know your statistics, insert info, otherwise GAME OVER: ")
        print()
        if info.lower() == "info":
            print()
            print(f"* {self.ranking()} * {self.username}")
            ll = SingleLinkedList()
            for key, value in self.game["players"][self.username].items():
                if type(value) != list:
                    ll.insert_last(f"{key}: {value}")
            ll.print_list()
            print()
        print("Thanks for playing. See you next time!")
        exit()

    def ranking(self):
        if self.points < 100:
            self.rank = "BEGINNER"
        elif self.points in range(100,200):
            self.rank = "SPECIALIST"
        elif self.points in range(200,300):
            self.rank = "MASTER"
        elif self.points in range(300,400):
            self.rank = "KING"
        elif self.points >= 400:
            self.rank = "GENIUS"
        return self.rank


class Process(Json):

    def __init__(self, hidden, changing, guesses,failed_guesses, list_of_categories, list_of_players,username, category, word, points):
        super().__init__(list_of_categories, list_of_players, username, category, word, points)
        self.hidden = hidden
        self.changing = changing
        self.guesses = guesses
        self.failed_guesses = failed_guesses
        self.letter = ""

    def letter_guessing(self):
        index = 0
        for i in self.word:
            if self.letter[0] == i:
                self.hidden[index] = self.letter[0]
                index += 1
            else:
                index += 1

    def deleting_list_duplicates(self):
        new_word = []
        for i in self.word:
            if i not in new_word:
                new_word.append(i)
        return len(new_word)

    def quantity_of_letters(self):
        quantity = 0
        for i in self.word:
            if i == self.letter:
                quantity += 1
        return quantity

    def hint_uncover_letter(self):
        for i in self.word:
            if self.word.count(i) == 1 and i not in self.hidden:
                self.hidden[self.word.index(random.choice(i))] = self.word[self.word.index(random.choice(i))]
                break
        return "".join(self.hidden)

    def process(self, start):
        while True:
            self.letter = input("Please input a letter: ")
            print()
            if len(self.letter) != 1:
                print("Please input only one letter", end="\n\n")
            else:
                if self.letter[0] in self.hidden:
                    print(f"You have already guessed that letter.", end="\n\n")
                else:
                    self.letter_guessing()
                    self.hidden = "".join(self.hidden)
                    self.changing = "".join(self.changing)
                    if self.hidden == self.changing:
                        self.points -= 3
                        print(f'There is no such letter, the hidden word is still {self.hidden}. You have {self.points} points', end="\n\n")
                        self.guesses += 1
                        self.failed_guesses += 1
                    else:
                        if self.hidden == self.word:
                            if self.guesses == self.deleting_list_duplicates():
                                self.points += 20 + 5 * 5 * self.quantity_of_letters()
                                print(f'''Wow, you are so smart. You have not guessed incorrectly even once. 
That is why you get additional 20 points. The word was {self.word} and it took you {self.guesses} guesses. You have {self.points} points''', end="\n\n")
                            else:
                                self.points += 5 * self.quantity_of_letters()
                                print(f"Nice, you won!The word was {self.word} and it took you {self.guesses} guesses. You have {self.points} points", end="\n\n")
                            self.list_of_players[self.username]["points"] = self.points
                            start.json_dump()
                            start.ranking()
                            start.information_getting()
                        else:
                            self.points += 5 * self.quantity_of_letters()
                            print(f'Cool, you are right, the word is now {self.hidden}. You have {self.points} points', end="\n\n")
                            self.failed_guesses = 0
                            self.guesses += 1
                    if self.failed_guesses == 5:
                        hint = input(f"""It seems like you have some difficulties with guessing that word. Would you like to take a hint?
type yes if you do, otherwise you will not get it: """)
                        print()
                        if hint.lower() == 'yes':
                            self.hidden = list(self.hidden)
                            self.changing = list(self.changing)
                            self.points -= 10
                            print(f"I uncover one random letter for you, now the hidden word is {self.hint_uncover_letter()}.You have {self.points} points", end="\n\n")
                            self.changing = self.hidden
                        self.failed_guesses = 6
                    self.changing = self.hidden
                    self.hidden = list(self.hidden)
                    self.changing = list(self.changing)


def main():
    start = Json(Json.game["categories"], Json.game["players"], "", "", "", 0)
    start.username_picking()
    start.category_picking()
    start.defining_rules()
    process = Process(list("*" * len(start.word)), list("*" * len(start.word)), 1, 0, Json.game["categories"], Json.game["players"], start.username, start.category, start.word, start.points)
    process.process(start)


main()








