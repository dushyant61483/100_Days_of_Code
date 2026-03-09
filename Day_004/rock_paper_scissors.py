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

lst = ["rock", "paper", "scissors"]
user_input = input("What do you choose? ").lower()
computer = random.choice(lst)
if user_input == "rock":
    print(f"You choose 'ROCK'\n\n{rock}")
elif user_input == "paper":
    print(f"You choose 'PAPER'\n\n{paper}")
elif user_input == "scissors":
    print(f"You choose 'SCISSORS'\n\n{scissors}")
else:
    print("Wrong Input")

if computer == "rock":
    print(f"Computer choose 'ROCK'\n\n{rock}")
elif computer == "paper":
    print(f"Computer choose 'PAPER'\n\n{paper}")
else:
    print(f"Computer choose 'SCISSORS'\n\n{scissors}")

if computer == user_input:
    print("Draw")
elif computer == "rock" and user_input == "paper":
    print("You win!!")
elif computer == "rock" and user_input == 'scissors':
    print("You lose!!")
elif computer == "paper" and user_input == "rock":
    print("You lose!!")
elif computer == "paper" and user_input == "scissors":
    print("You win!!")
elif computer == "scissors" and user_input == "rock":
    print("You win!!")
elif computer == "scissors" and user_input == "paper":
    print("You lose!!")
else:
    print("Error")
