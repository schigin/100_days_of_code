from art import logo
# import os

print(logo)
print("\nWelcome to the secret auction program.")

new_bidder = True
bidders = {}
while new_bidder:
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid

    result = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    # os.system('clear')
    if result == 'no':
        new_bidder = False

        winner = None
        highest_bid = 0
        for name in bidders:
            if bidders[name] > highest_bid:
                winner = name
                highest_bid = bidders[name]
        print(f"The winner is {winner} with a bid of ${bidders[winner]}.")
