import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

while(True):
    n1 = int(input("Enter your first number: "))
    while True:

        print("+\n-\n*\n/")
        oper = input("Enter your operation: ")
        n2 = int(input("Enter your second number: "))
        if oper == "+":
            result = add(n1, n2)
        elif oper == "-":
            result = subtract(n1, n2)
        elif oper == "*":
            result = multiply(n1, n2)
        elif oper == "/":
            if n2==0:
                print("Divided by zero Cannot divide by zero\n")
                n2 = int(input("Enter your second number: "))
                result = divide(n1, n2)
            else:
                result = divide(n1, n2)
        print("Your result is: ", result)
        again = input(f"Do you want to continue the calculation with {result}(y/n): ")
        if again == "y":
            n1 = result
        if again == "n":
            break
