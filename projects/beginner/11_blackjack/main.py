############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card = random.choice(cards)
    return new_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(your_score, dealer_score):
    if your_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"

    if your_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif your_score == 0:
        return "Win with a Blackjack 😎"
    elif your_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif your_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def blackjack():
    print(logo)
    your_cards = []
    dealer_cards = []
    is_game_over = False

    for i in range(2):
        your_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        your_score = calculate_score(your_cards)
        dealer_score = calculate_score(dealer_cards)

        if your_score > 21 or your_score == 0 or dealer_score == 0:
            is_game_over = True
        else:
            print(f"\tYour cards: {your_cards}, current score: {your_score}")
            print(f"\tComputer's first card: {dealer_cards[0]}")

            next_step = input("Type 'y' to get another card, type 'n' to pass: ")
            if next_step == 'n':
                is_game_over = True
            else:
                your_cards.append(deal_card())


    while dealer_score < 17 and dealer_score != 0:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"\tYour final hand: {your_cards}, final score: {your_score}")
    print(f"\tComputer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(your_score, dealer_score))


play_game = True
while play_game:
    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if new_game == 'y':
        blackjack()
    else:
        play_game = False

