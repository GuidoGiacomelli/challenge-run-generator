import random
import json
with open("games.json", "r") as file:
    games = json.load(file)

def display_games(games):
    print("Available games: ")
    for g in games.keys():
        print(f"- {g.title()}")

def get_challenge(games, game):
    return random.choice(games[game])

while True:
    print("Challenge run generator")
    display_games(games)
    game = input("Select a game: ")
    game = game.lower()
    if game in games:
        print(f"Your challenge: {get_challenge(games, game)}")
    else:
        print("Game is not available yet")
    while True:
        choice = input("Do you want to continue? (y/n)")
        if choice.lower() == "y":
            break
        elif choice.lower() == "n":
            print("Process finished")
            exit()
        else:
            print("Invalid input. Try again")
