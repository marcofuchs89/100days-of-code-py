# Blind/Sealed Auction
from typing import Dict
from art import logo
from os import system

# initialize needed helper variables
winner = ""
highest_bid = 0
new_auctioneer = True
bid_register = {}

if __name__ == "__main__":
    print(logo)
    print("Welcome to the sealed auction!")

    while new_auctioneer:
        user_name = input("What's your name?: ")
        bid_amount = int(input("What's your bid price?: $"))
        bid_register[user_name] = bid_amount
        another_auctioneer = input(
            "Is there another person who want's to bid? (yes/no): "
        )
        if another_auctioneer == "no":
            new_auctioneer = False
        system("clear")

    for user in bid_register:
        if bid_register[user] > highest_bid:
            highest_bid = bid_register[user]
            winner = user
        else:
            pass

    print(f"{winner} has won the auction with a bid of ${highest_bid}")
