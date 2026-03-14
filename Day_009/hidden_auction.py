import art
print(art.logo)
# TODO-1: Ask the user for input
auction = {}
while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))

# TODO-2: Save data into dictionary {name: price}
    auction[name] = bid
# TODO-3: Whether if new bids need to be added
    again = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if again == "no":
        break
    else:
        print("\n"*20)
# TODO-4: Compare bids in dictionary


for key, value in auction.items():
    maximum = 0
    name = ""
    if value > maximum:
        name ,maximum = key , value

print(f"The winner is {name} with a bid of ${maximum}")
