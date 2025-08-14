import os

print("Welcome to bidding!")
bidders_dict = {}
should_continue = True
while should_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bidders_dict[name] = bid
    ans = input("Is there any other bidder? Y or N: ")

    if ans == "Y":
        should_continue = True
    elif ans == "N":
        should_continue = False
    else:
        print("Invalid input")

    os.system("clear")

#Check who won and print
for name in bidders_dict:
    highest_bid = 0
    highest_bidder = ""
    if bidders_dict[name] > highest_bid:
        highest_bid = bidders_dict[name]
        highest_bidder = name

print("Highest bidder: ", highest_bidder)



