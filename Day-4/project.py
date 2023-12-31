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

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
program_choice = random.randint(0, 2)
options = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
else:
  print(options[user_choice])
  print(f"Computer chose: {program_choice}")
  print(options[program_choice])

  if user_choice == 0 and program_choice == 0:
    print("You win!")
  elif program_choice == 0 and user_choice == 2:
    print("You lose!")
  elif program_choice > user_choice:
    print("You lose!")
  elif user_choice > program_choice:
    print("You win!")
  elif program_choice == user_choice:
    print("It's a draw!")
  
