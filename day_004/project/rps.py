# Import choice from random() to generate the computer choice
from random import choice, randint

# Visual representation of the pick
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Representation of a game board (decision making)
# Human choice is on the colums -> 0: rock, 1: paper, 2: scissors
# Computer choice is on the rows -> 0: rock, 1: paper, 2: scissors
# Results -> 0: draw, 1: human wins, -1: computer wins
row1 = [0, -1, 1]
row2 = [1, 0, -1]
row3 = [-1, 1, 0]

game_board = [row1, row2, row3]

# Map out the possible hands for easy selection
playable_hands = [rock, paper, scissors]


# Start the game
if __name__ == '__main__':
    # Welcome and picking the hands
    print("Welcome to pRPS - Pythonic Rock, Paper, Scissors!")
    human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = randint(0, 2)

    if human_choice not in (0, 1, 2):
        print("Wrong input ... you have to start over")
    else:
        # Printing the made choices
        print("\nYour choice:")
        print(playable_hands[human_choice])

        print("\nComputers choice:")
        print(playable_hands[computer_choice])

        # Determining win, loss or draw
        if game_board[human_choice][computer_choice] == 1:
            print("You win. Congratulations!")
        elif game_board[human_choice][computer_choice] == -1:
            print("You lose. Sorry!")
        elif game_board[human_choice][computer_choice] == 0:
            print("It's a draw. Next round!")
