import random

games = {
    "resident evil 1": [
        "Invisible Enemy",
        "Handgun only (No defense items)",
        "Knife only",
        "Shotgun only",
        "Kill less than 20 enemies (Counting bosses)",
        "Finish the game in less than 3 hours",
        "Finish the game with the best ending in less than 4 hours",
        "Finish the game without ever burning a body",
        "Finish the game without ever killing a hunter"],
    "resident evil 2": [
        "No defense items (Remake only)",
        "Handgun only (No defense items)",
        "Knife only (Infinite knife allowed)",
        "Shotgun / Grenade launcher only",
        "Kill less than 20 enemies (Counting bosses)",
        "Finish the game without ever killing a licker",
        "Finish the game without killing ANY enemies in the sewers (Alligator and G2 excluded)",
        "Magnum / SMG only",
        "S+ on Hardcore (Remake only)"],
    "resident evil 4": [
        "Handgun only (Knife allowed)",
        "Shotgun only",
        "Knife only (Primal and Melee allowed)",
        "Rifle only",
        "No merchant",
        "All treasures",
        "S+ on Pro (Remake only)",
        "Bolt thrower only (Any weapon until available)"
    ]
}

while True:
    print("Challenge run generator")
    print("Available games: ")
    for g in games.keys():
        print(f"- {g.title()}")
    game = input("Select a game: ")
    game = game.lower()
    if game.lower() in games:
        challenge = random.choice(games[game])
        print(f"Your challenge: {challenge}")
    else:
        print("Game is not available yet")
    while True:
        ("Do you want to continue? (y/n)")
        choiceinp = input("Do you want to continue? (y/n)")
        if choiceinp.lower() == "y":
            break
        elif choiceinp.lower() == "n":
            print("Process finished")
            exit()
        else:
            print("Invalid input. Try again")
