rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice < 0 or choice >= 3:
    print("You typed an invalid number. You lose.")
else:
    print(game_images[choice])
    comp_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[comp_choice])

    if choice == comp_choice:
        print('Draw')
    elif (choice == 0 and comp_choice == 2) or (choice == 1 and comp_choice == 0) or (choice == 2 and comp_choice == 1):
        print('You win')
    else:
        print('You lose')


