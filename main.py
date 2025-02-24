from art import logo
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide

    }
def calculator():
    print(logo)
    end_of_loop = False
    num1 = float(input("what is first number "))
    while not end_of_loop:
        
        num2 = float(input("what is second number "))

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Please pick the operation above mention ")

        function = operations[operation_symbol]
        answer = function(n1=num1, n2= num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        result = input(f"Did you want to continue with the {answer} 'y' or start new calculation 'no'")
        if result ==  "y":
            num1 = answer
        else:
            end_of_loop = True
            calculator()
        

calculator()