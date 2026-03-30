from art import logo
print(logo)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money" : 0
}


def to_resource_update(order):
    to_update = True
    for key,value in MENU[order]["ingredients"].items():
        if resources[key] < value:
            if key == "water" or key == "milk":
                print(f"Sorry {key} is less than {value}ml")
            elif key == "coffee":
                print(f"Sorry {key} is less than {value}g")
            to_update = False
    return to_update

def show_report():
    print(f"Water: {resources['water']}ml" )
    print(f"Milk: {resources['milk']}ml" )
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def order_confirm(order):
    to_confirm = True
    order_cost = MENU[order]["cost"]
    quarters = .25
    dimes = .10
    nickles = .05
    pennies = .01
    change = 0
    if to_confirm:
        print("Please insert Coins")
        while True:
            total = 0
            quarters_no = int(input("How many quarters?: "))
            dimes_no = int(input("How many dimes?: "))
            nickles_no = int(input("How many nickles?: "))
            pennies_no = int(input("How many pennies?: "))

            total = quarters_no * quarters + dimes_no*dimes + nickles_no * nickles + pennies_no * pennies
            if total > order_cost:
                change = total-order_cost
                break
            elif total < order_cost:
                print("Your Amount is too low\nMoney is refunding....")
                confirm = input("Do you want to cancel order? (y/n): ").lower()
                if confirm == "y":
                    return resources
                else:
                    print("Kindly Pay Again")
            else:
                change = 0
                break
        for key, value in MENU[order]["ingredients"].items():
            resources[key] -= value

        resources["money"] += order_cost
        print(f"Here is Your {order}")
        if change == 0:
            pass
        else:
            print(f"Your change is {change}")
        return resources


while True:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order in ["espresso", "latte", "cappuccino"]:
        if to_resource_update(user_order):
            print(f"The amount for {user_order} is {MENU[user_order]["cost"]}")
            resources = order_confirm(user_order)
    elif user_order == "report":
        show_report()
    elif user_order == "off":
        print("Machine is going to Power off")
        break
    else:
        print("Sorry, that's not a valid option.")
