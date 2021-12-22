# Create a calculator.
# Crie uma calculadora.

def operations():
    if option == "add":
        result = str(num1 + num2)
    elif option == "sub":
        result = str(num1 - num2)
    elif option == "mul":
        result = str(num1 * num2)
    else:
        result = str(num1 / num2)
    return result


program = "on"
while program == "on":

    print()
    print("Options:")
    print("Type 'add' to add:")
    print("Type 'sub' to subtract:")
    print("Type 'mul' to multiply:")
    print("Type 'div' para divide:")
    print("Type 'q' to quit:")

    option = input()

    if option == "q":
        program = "off"

    elif option == "add" or option == "sub" or option == "mul" or option == "div":
        print()
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = operations()
        print("The result is: " + result)
        menu = "on"

    else:
        print("Unknown expression.")
        print("Try again:")
        menu = "off"

    while menu == "on":
        print()
        print("Do you want to do another operation?")
        question = input("Type 'y' to yes e 'n' for no: ")
        if question == "n":
            menu = "off"
            program = "off"
        elif question == "y":
            menu = "off"
        else:
            print("Unknown expression.")
            print("Try again:")


