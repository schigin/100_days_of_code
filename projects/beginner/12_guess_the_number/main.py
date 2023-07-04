from art import logo
import random

N_ATTEMPTS_EASY = 10
N_ATTEMPTS_HARD = 5


def check_answer(user_guess, correct_number, n_attempts):
    if user_guess == correct_number:
        print(f"You got it! The answer was {correct_number}.")
        return n_attempts
    else:
        if user_guess < correct_number:
            print("Too low.")
        else:
            print("Too high.")
        return n_attempts - 1


def set_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == 'easy':
        return N_ATTEMPTS_EASY
    else:
        return N_ATTEMPTS_HARD


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!"
          "\nI'm thinking of a number between 1 and 100.")

    number = random.randint(1, 101)
    print(f"Pssst, the correct answer is {number}")

    n_attempts = set_difficulty()

    user_number = 0
    while user_number != number:
        print(f"You have {n_attempts} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        n_attempts = check_answer(user_number, number, n_attempts)

        if n_attempts == 0:
            print("You've run out of guesses, you lose.")
            return

        elif user_number != number:
            print("Guess again.")


game()


