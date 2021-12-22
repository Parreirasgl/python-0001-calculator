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

while True:

    print()
    print("Options:")
    print("Type 'add' to add:")
    print("Type 'sub' to subtract:")
    print("Type 'mul' to multiply:")
    print("Type 'div' para divide:")
    print("Type 'q' to quit:")

    option = input()

    if option == "q":
        break

    elif option == "add" or option == "sub" or option == "mul" or option == "div":
        print()
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = operations()
        print("The result is: " + result)

    else:
        print("Unknown expression")
        print("Try again")
        continue


