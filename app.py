import random
import json


def quantity_of_letters(letter, list):
    quantity = 0
    for i in list:
        if i == letter:
            quantity += 1
    return quantity


def deleting_list_duplicates(list):
    new_word = []
    for i in list:
        if i not in new_word:
            new_word.append(i)
    return len(new_word)


def finding_most_frequent(list):
    counter = 0
    num = list[0]
    for i in list:
        curr_frequency = list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num


def letter_guessing(word, letter, hidden):
    index = 0
    for i in word:
        if letter[0] == i:
            hidden[index] = letter[0]
            index += 1
        else:
            index += 1


def hint_uncover_letter(a, b):
    for i in b:
        if b.count(i) == 1 and i not in a:
            a[b.index(random.choice(i))] = b[b.index(random.choice(i))]
            break
    return "".join(a)


def json_dump(game):
    with open('app.json', 'w') as outfile:
        json.dump(game, outfile, indent=2)


def json_load():
    with open('app.json') as json_file:
        game = json.load(json_file)
    return game


def username_picking(game, username):
    for i in range(0, len(game)+1):
        if username not in game["players"]:
            game["players"][username] = {"points": 50, "favorite_category": "", "words_guessed": [], "categories_picked": []}
    return game, username


def category_picking(game, username):
    print(f'''Hello {username}, lets play a game. To start, you need to pick a category.''')
    number = 1
    for i in game["categories"].keys():
        print(f"{number}. {i}")
        number += 1
    category = input("Please pick a category: ")
    while True:
        if category not in game["categories"]:
            category = input("There is no such category. Please pick again: ")
        else:
            break
    return category


def json_adding_data(game, username, category):
    game["players"][username]["categories_picked"].append(category)
    game["players"][username]["favorite_category"] = finding_most_frequent(game["players"][username]["categories_picked"])
    return game, username, category


def rules(game, username, category, word):
    print(f"""
For each guessed letter you will earn 5 points.
For each failed guess you will lose 3 points.
For a taken hint you will lose 10 points.
IF you guess the word with no failed guesses, you additionaly get 20 points.
Good luck, now you have {game["players"][username]["points"]} points
""")
    print(f"Now i think of a word under the category {category}. It is {len(word)} characters long. ")


def information_getting(game, username):
    info = input("If you want to know your statistics, insert info, otherwise GAME OVER: ")
    if info.lower() == "info":
        print(f"username: {username}")
        for key, value in game["players"][username].items():
            if type(value) != list and type(value) != dict:
                print(key, ": ", value)
        exit()
    else:
        exit()


def process(hidden, changing, game, username, word, guesses, failed_guesses):
    while True:
        letter = input("Please input a letter: ")
        if len(letter) > 1:
            print("Please input only one letter")
        elif letter[0] in hidden:
            print(f"You have already guessed that letter.")
        else:
            letter_guessing(word, letter, hidden)
            hidden = "".join(hidden)
            changing = "".join(changing)
            if hidden == changing:
                game["players"][username]["points"] -= 3
                print(f'I am very sorry but there is no such letter, the hidden word is still {hidden}. You have {game["players"][username]["points"]} points')
                guesses += 1
                failed_guesses += 1
            else:
                if hidden == word:
                    deleting_list_duplicates(word)
                    if guesses == deleting_list_duplicates(word):
                        game["players"][username]["points"] += 20
                        print(
                            f"Wow, you are so smart. You have not guessed incorrectly even once. That is why you get additional 20 points. The word was {word}, number of guesses {guesses}. You have {game['players'][username]['points']} points")
                        game["players"][username]["words_guessed"].append(word)
                        json_dump(game)
                        information_getting(game, username)
                    else:
                        game["players"][username]["points"] += 5 * quantity_of_letters(letter, word)
                        print(f"Nice, you won, word was {word}, number of guesses {guesses}. You have {game['players'][username]['points']} points")
                        game["players"][username]["words_guessed"].append(word)
                        json_dump(game)
                        information_getting(game, username)
                else:
                    game["players"][username]['points'] += 5 * quantity_of_letters(letter, word)
                    print(f'Cool, you are right, the word is now {hidden}. You have {game["players"][username]["points"]} points')
                    failed_guesses = 0
                    guesses += 1
            if failed_guesses == 5:
                hint = input(f"""
It seems like you have some difficulties with guessing that word. Would you like to take a hint?
type yes if you do, otherwise you will not get it: """)
                if hint.lower() == 'yes':
                    game["players"][username]['points'] -= 10
                    hidden = list(hidden)
                    changing = list(changing)
                    print(f"I uncover one random letter for you, not the hidden word is {hint_uncover_letter(hidden,word)}.You have {game['players'][username]['points']} points")
                    changing = hidden
                    failed_guesses = 6
                if hint.lower() == "no":
                    failed_guesses = 6
            changing = hidden
            hidden = list(hidden)
            changing = list(changing)


def main():
    game = json_load()
    username = input("Please input your username: ")
    username_picking(game, username)
    category = category_picking(game, username)
    json_adding_data(game, username, category)
    word = game["categories"][category.lower()][random.randint(0, -1 + len(game["categories"][category.lower()]))]
    hidden = list("*" * len(word))
    changing = list("*" * len(word))
    guesses = 1
    failed_guesses = 0
    rules(game, username, category, word)
    process(hidden, changing, game, username, word, guesses, failed_guesses)


main()
