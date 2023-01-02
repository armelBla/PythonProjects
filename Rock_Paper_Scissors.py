import random

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

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(f"player choose:\n {player_choice}")

option = [rock, paper, scissors]
player_decision = option[player_choice]
print(player_decision)

computer_choice = random.randint(0, 2)
computer_decision = option[computer_choice]
print(f"Computer choose:\n {computer_choice}")
print(computer_decision)

if (player_choice == 0) and (computer_choice == 1):
    print("You lose")
elif (player_choice == 0) and (computer_choice == 2):
    print("You win")
elif (player_choice == 1) and (computer_choice == 2):
    print("You lose")
elif (player_choice == 2) and (computer_choice == 1):
    print("You win")
else:
    print("Draw")
