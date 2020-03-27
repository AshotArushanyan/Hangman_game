import random
import json

with open('app.json') as json_file:
    game = json.load(json_file)

def unique_set(list):
    new_word = []
    for i in list:
        if i not in new_word:
            new_word.append(i)
    return len(new_word)


def most_frequent(list):
    counter = 0
    num = list[0]
    for i in list:
        curr_frequency = list.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


def letter_guessing():
    index = 0
    for i in word:
        if letter[0] == i:
            hidden[index] = letter[0]
            index += 1
        else:
            index += 1


def hint_yes(a, b):
    for i in b:
        if b.count(i) == 1 and i not in a:
            a[b.index(random.choice(i))] = b[b.index(random.choice(i))]
            break
    return "".join(a)


dictionary = {
    "countries": ["afghanistan","albania","algeria","andorra","angola","argentina","armenia","australia","austria","azerbaijan","bahamas","bahrain","bangladesh","barbados","belarus"],
    "flowers": [],
    "fruits": [],
    "vegetables": [],
    "animals": [],
    "weapons": [],
    "sports": [],
}

username = input("Please input your username: ")
for i in range(0, len(game)+1):
    if username in game:
        pass
    else:
        game[username] = {"points": 50, "favorite_category": "", "words_guessed": [], "categories_picked": []}
print(f'''Hello {username}, lets play a game. To start, you need to pick a category

Categories:
1. Countries
2. Flowers
3. Fruits
4. Vegetables
5. Animals
6. Weapons
7. Sports
''')
category = input("Please pick a category: ")
game[username]["categories_picked"].append(category)
game[username]["favorite_category"] = most_frequent(game[username]["categories_picked"])
while True:
    if category not in game["categories"]:
        category = input("There is no such category. Please pick again: ")
    else:
        break
word = game["categories"][category.lower()][random.randint(0, -1+len(game["categories"][category.lower()]))]
hidden = list("*" * len(word))
changing = list("*" * len(word))
guesses = 1
failed_guesses = 0
print(f"""You have {game[username]["points"]} points. 
For each guessed letter you will earn 5 points.
For each failed guess you will lose 3 points. 
For a taken hint you will lose 10 points. 
IF you guess the word with no failed guesses, you additionaly get 20 points. 
Good luck, now you have {game[username]["points"]} points""")
print(f"Now i think of a word under the category {category}. It is {len(word)} characters long. ")
while True:
    letter = input("Please input a letter: ")
    if len(letter) != 1:
        print("Please input only one letter")
    elif letter[0] in hidden:
        print(f"You have already guessed that letter.")
    else:
        letter_guessing()
        hidden = "".join(hidden)
        changing = "".join(changing)
        if hidden == changing:
            game[username]["points"] -= 3
            print(f'I am very sorry but there is no such letter, the hidden word is still {hidden}. You have {game[username]["points"]} points')
            guesses += 1
            failed_guesses += 1
        else:
            if hidden == word:
                unique_set(word)
                if guesses == unique_set(word):
                    game[username]["points"] += 20
                    print(f"Wow, you are so smart. You have not guessed incorrectly even once. That is why you get additional 20 points. The word was {word}, number of guesses {guesses}. You have {game[username]['points']} points")
                    game[username]["words_guessed"].append(word)
                    with open('app.json', 'w') as outfile:
                        json.dump(game, outfile)
                    exit()
                else:
                    print(f"Nice, you won, word was {word}, number of guesses {guesses}. You have {game[username]['points']} points")
                    game[username]["words_guessed"].append(word)
                    with open('app.json', 'w') as outfile:
                        json.dump(game, outfile)
                    exit()
            else:
                game[username]['points'] += 5
                print(f'Cool, you are right, the word is now {hidden}. You have {game[username]["points"]} points')
                failed_guesses = 0
                guesses += 1
        if failed_guesses == 5:
            hint = input(f"It seems like you have some difficulties with guessing that word. Would you like to take a hint? yes/no ")
            if hint.lower() == 'yes':
                game[username]['points'] -= 10
                hidden = list(hidden)
                changing = list(changing)
                print(f"I uncover one random letter for you, not the hidden word is {hint_yes(hidden, word)}. You have {game[username]['points']} points")
                changing = hidden
                failed_guesses = 6
            if hint.lower() == "no":
                failed_guesses = 6
        changing = hidden
        hidden = list(hidden)
        changing = list(changing)

