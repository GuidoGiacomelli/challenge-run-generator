import random
import json
from unittest import case
with open("games.json", "r") as file:
    games = json.load(file)

def display_games(games):
    print("Available games: ")
    for g in games.keys():
        print(f"- {g.title()}")

def get_challenge(games, game_name):
    return random.choice(games[game_name])

def add_challenge(games, game_name, challenge):
    if game_name not in games:
        games[game_name] = []
    games[game_name].append(challenge)
    with open("games.json", "w") as file:
        json.dump(games, file, indent=4)
    print("Challenge added successfully.")

while True:
    print("Challenge run generator\n1. Show game list\n2. Get a challenge\n3. Add a challenge\n4. Exit")
    match input("Select an option: "):
        case "1":
            display_games(games)
        case "2": 
            game_name = input("Select a game: ").lower()
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
        case "3":
            game_name = input("Select a game: ").lower()
            challenge = input("Enter a new challenge: ")
            add_challenge(games, game_name, challenge)
        case "4":
            print("Process finished")
            exit()