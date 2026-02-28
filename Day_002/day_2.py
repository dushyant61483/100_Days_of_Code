print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))

ans = (bill/people)*(tip/100)
print("Your tip is",ans)
ans = ans + bill/people
print(f"Each person should pay: ${ans}")
