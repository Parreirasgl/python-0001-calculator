# Create a calculator.
# Crie uma calculadora.

while True:

    print()
    print("Options:")
    print("Type 'add' to add:")
    print("Type 'sub' to subtract:")
    print("Type 'mul' to multiply:")
    print("Type 'div' para divide:")
    print("Type 'q' to quit:")

    x = input()

    if x == "q":
        break

    elif x == "add":
        print()
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = str(num1 + num2)
        print("The result is: " + result)

    elif x == "sub":
        print()
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = str(num1 * num2)
        print("The result is: " + result)

    elif x == "mul":
        print()
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = str(num1 * num2)
        print("The result is: " + result)

    elif x == "div":
        print()
        num1 = float(input("Type a number: "))
        num2 = float(input("Type another number: "))
        result = str(num1 / num2)
        print("The result is: " + result)

    else:
        print("Unknown expression")
        print("Try again")
        continue


