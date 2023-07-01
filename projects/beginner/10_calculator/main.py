from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        result = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation "
        "or type 'exit' to stop the program: ")
        if result == 'y':
            num1 = answer
        elif result == 'n':
            should_continue = False
            calculator()
        elif result == 'exit':
            should_continue = False


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

calculator()