import random
from game_data import data
import art

def greeting():
    print(art.logo)

def game():
    score = 0
    competitor1 = random.choice(data)
    competitor2 = random.choice(data)
    if competitor1 == competitor2:
        competitor1 = random.choice(data)

    while True:
        print("\n" * 20)
        greeting()
        print(f"Current Score = {score}")
        print(f"Compare A : {competitor1["name"]} , {competitor1['description']} , {competitor1['country']}")
        one_follower = competitor1["follower_count"]
        print(art.vs)
        print(f"Against B : {competitor2["name"]} , {competitor2['description']} , {competitor2['country']}")
        two_follower = competitor2["follower_count"]
        while True:
            choice = input("Who has more followers? Type 'A' or 'B': ").lower()
            if choice == 'a':
                break
            elif choice == 'b':
                break
            else:
                print("Please type 'A' or 'B'.")

        if choice == "a":
            if one_follower > two_follower:
                score += 1
                competitor2 = random.choice(data)
            else:
                print("You Guessed wrong!! \nGame over\nFinal Score:", score)
                break
                break
        elif choice == "b":
            if one_follower < two_follower:
                score += 1
                competitor1 = competitor2
                competitor2 = random.choice(data)
            else:
                print("You Guessed wrong!! \nGame over\nFinal Score:", score)
                break

game()
while True:
    while True:
        again = input("Would you like to play again? Type 'Y' or 'N':").lower()
        if again == 'y':
            break
        elif again == 'n':
            break
        else:
            print("Please type 'Y' or 'N'.")

    if again == 'y':
        print("\n"*20)
        game()
    else:
        print("Thank you for playing!")
        break
