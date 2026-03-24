import random
from art import logo
def greeting():
    """This will be used for entrance"""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")


def take_input():
    """This will take input from user"""
    user_input = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return user_input

def integer():
    """For guessing the number """
    return random.randint(1,100)


def mode():
    """To set difficulty"""
    user_input = take_input()

    if user_input == "easy":
        return 10
    else:
        return 5

def guessing_game():
    greeting()
    num = integer()
    live = mode()
    while True:
        print(f"You have {live} attempts remaining to guess the number.")
        guessed_num = int(input("Make a guess: "))
        if guessed_num == num:
            print(f"You guessed the number CORRECTLY! = {num}")
            break
        elif guessed_num > num:
            print(f"You guessed too high!")
            live = live-1
        elif guessed_num < num:
            print(f"You guessed too low!")
            live = live-1
        if live == 0:
            print("Game Over! You ran out of lives!")
            break


guessing_game()
while True:
    again = input("Do you want to play again? (y/n): ")
    if again == "y":
        print("\n"*20)
        guessing_game()
    else:
        print("Thank you for playing!")
        break
