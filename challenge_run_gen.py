import random
import json
with open("games.json", "r") as file:
    games = json.load(file)

def display_games(games):
    print("Available games: ")
    for g in games.keys():
        print(f"- {g.title()}")

def get_challenge(games, game_name):
    return random.choice(games[game_name])

while True:
    print("Challenge run generator")
    display_games(games)
    game_name = input("Select a game: ")
    game_name = game_name.lower()
    if game_name in games:
        print(f"Your challenge: {get_challenge(games, game_name)}")
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
