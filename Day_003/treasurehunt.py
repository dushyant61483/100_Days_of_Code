print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction  = input("Choose the direction you want to take the treasure: (left/right)")
if direction == "left":
    print("Now you have reached near the Ocean!!")
    want_to_do = input("Do you want to wait for the boat or reach there by swimming (wait/swim)")
    if want_to_do == "wait":
        print("You reached safely on the Island")
        choose_door = input("Which door you want to open (red/blue/yellow): ")
        if choose_door == "red":
            print("You get caught in the fire\nGame Over")
        elif choose_door == "blue":
            print("You fell down in the ocean\nGame Over")
        else:
            print("You win the treasure!! Yeah you deserve it\nYou are the wealthiest person")
    else:
        print("You drown in the ocean\Game Over")

else:
    print("You fall into a hole.\nGame Over")
