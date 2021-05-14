print('''

     ____________________________________________________
    |____________________________________________________|
    | __     __   ____   ___ ||  ____    ____     _  __  |
    ||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |
    ||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |
    ||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |
    ||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|
    ||_______________________||__________________________|
    | _____________________  ||      __   __  _  __    _ |
    ||=|=|=|=|=|=|=|=|=|=|=| __..\/ |  |_|  ||#||==|  / /|
    || | | | | | | | | | | |/\ \  \\\\|++|=|  || ||==| / / |
    ||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|
    |____________________ /\~()/()~//\ __________________|
    | __   __    _  _     \_  (_ .  _/ _    ___     _____|
    ||~~|_|..|__| || |_ _   \ //\\\\ /  |=|__|~|~|___| | | |
    ||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|
    ||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|
    |_________________ _/    \/\/\/    \_ _______________|
    | _____   _   __  |/      \../      \|  __   __   ___|
    ||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||
    ||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||
    ||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||
    |_________ __________\___\____/___/___________ ______|
    |__    _  /    ________     ______           /| _ _ _|
    |\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|
    | \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|
  __|  \/\|/   /(____|/ //                    /  /||~|~|~|__
    |___\_/   /________//   ________         /  / ||_|_|_|
    |___ /   (|________/   |\_______\       /  /| |______|
        /                  \|________)     /  / | |

Edward the Librarian greets you heartly as you enter the historian library of Leicester!
You'll begin your journey by choosing a book/story and continue reading.
Maybe you'll find something interesting on those pages .. ;)\n
''')

story_line = input("Which story line would you like to read on? [A]dventure, [M]ythic or [R]oman\n")

if story_line.lower() == "a":
    print("Edward hands you a book with the title: 'Jumanji'")
    print("As it touches your hands you immediately hear the sound of drums and chantings in your ears.")
    next_step = input("What will you do next? Do you dare to [open] the book or do you want to [inspect] it further?\n")
    if next_step.lower() == "open":
        pass
    elif next_step.lower() == "inspect":
        pass
    else:
        print("Wrong decision. Story-Time is over.")
    pass
elif story_line.lower() == "m":
    pass
elif story_line.lower() == "r":
    pass
else:
    print("You've picked the wrong story-line. Please come in again.")

