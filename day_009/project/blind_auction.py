# Blind/Sealed Auction
from art import logo
from os import system

# initialize needed helper variables
bidding_finished = False
bid_register = {}


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_register:
        if bid_register[bidder] > highest_bid:
            highest_bid = bid_register[bidder]
            winner = bidder

    print(f"{winner} has won the auction with a bid of ${highest_bid}")


if __name__ == "__main__":
    print(logo)
    print("Welcome to the sealed auction!")

    while not bidding_finished:
        user_name = input("What is your name?: ")
        bid_amount = int(input("What is your bid?: $"))
        bid_register[user_name] = bid_amount
        another_auctioneer = input(
            "Are there any other bidders? Type 'yes or 'no'.\n"
        ).lower()
        if another_auctioneer == "no":
            bidding_finished = True
            find_highest_bidder(bid_register)
        elif another_auctioneer == "yes":
            system("clear")
