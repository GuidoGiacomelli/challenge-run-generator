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
        "Finish the game without ever killing a hunter",
        "No saving (Normal)"
    ],
    "resident evil 2": [
        "No defense items (Remake only)",
        "Handgun only (No defense items)",
        "Knife only (Infinite knife allowed)",
        "Shotgun / Grenade launcher only",
        "Kill less than 20 enemies (Counting bosses)",
        "Finish the game without ever killing a licker",
        "Finish the game without killing ANY enemies in the sewers (Alligator and G2 excluded)",
        "Magnum / SMG only",
        "S+ on Hardcore (Remake only)",
        "No saving (Hardcore)",
        "No weapon modifications"
    ],
    "resident evil 3": [
        "Fight and down Nemesis EVERY time you encounter him (Heavy)",
        "Handgun only",
        "Shotgun only",
        "Heavy in less than 2 hours",
        "Kill NO enemies as Carlos",
        "No saving (Heavy)"
    ],
    "resident evil 4": [
        "Handgun only (Knife allowed)",
        "Shotgun only",
        "Knife only (Primal and Melee allowed)",
        "Rifle only",
        "No merchant",
        "All treasures",
        "S+ on Pro (Remake only)",
        "Bolt thrower only (Remake only)",
        "No killing any enemies until Del Lago",
        "Only save 5 times max (Pro)"
    ],
    "resident evil 7": [
        "Handgun only (Knife allowed)",
        "Shotgun only (Handgun or Knife for Mia Boss Fight)",
        "Knife only",
        "Madhouse in less than 4 hours",
        "Standard under 2:30 hours",
        "No saving (Standard)"
    ],
    "resident evil 8": [
        "Handgun only (Knife allowed)",
        "Shotgun only",
        "Knife only",
        "Hardcore under three hours",
        "No running in House Beneviento",
        "No duke",
        "Village of Shadows (fuck you)",
        "No saving (Hardcore)"
    ],
    "Silent Hill 2": [
        "Plank / Pipe only",
        "Handgun only",
        "Hard / Hard in less than 4 hours",
        "Finish the game without killing ANY mannequins",
        "Only save 3 times max (Combat hard)",
        "Get In Water ending in under 5 hours",
        "Get Maria ending in under 5 hours",
        "Get Leave ending in under 5 hours",
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
