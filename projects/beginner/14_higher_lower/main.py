from game_data import data
from art import logo
import random

def create_pair_for_comparison(data, a, b):
    if a:
        a = b
    else:
        a = random.choice(data)

    b = random.choice(data)

    while a == b:
        b = random.choice(data)
    return a, b

def game():
    print(logo)
    a = {}
    b = {}
    score = 0
    is_game_over = False

    while not is_game_over:
        a, b = create_pair_for_comparison(data, a, b)

        print(f"###### - Round {score + 1}")
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print("\nVS")
        print(f"\nAgainst B: {b['name']}, a {b['description']}, from {b['country']}.")
        answer = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if (answer == 'a' and a['follower_count'] > b['follower_count']) \
                or (answer == 'b' and b['follower_count'] > a['follower_count']):
            score += 1
            print(f"You're right! Current score: {score}.\n")
        else:
            is_game_over = True
            print(f"Sorry, that's wrong. Final score: {score}.")

game()
