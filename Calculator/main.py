from art import logo


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Now when we call function and pass 2 values it will be passed to the functions
# calculation_function = operations["*"]
# print(function(2, 3))


def calculator():
    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    # While loop that lets user continue infinitely with operations on the answer
    run = True
    while run:
        choice = input("Pick an operation: ")

        while choice not in operations:
            print("Invalid Choice")
            choice = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))
        calculation_function = operations[choice]
        answer = calculation_function(num1, num2)
        print(f"{num1} {choice} {num2} = {answer}")

        user_choice = input(f"Type 'y' to continue calculation with {answer} and 'n' for new calculation: ")
        if user_choice == 'n':
            # Using recursion to start from the beginning by calling itself
            calculator()
        num1 = answer


print(logo)
calculator()