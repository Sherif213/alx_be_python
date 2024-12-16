numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
match operator:
    case '+':
        print(f"The result is {numberOne + numberTwo}.")
    case '-':
        print(f"The result is {numberOne - numberTwo}.")
    case '*':
        print(f"The result is {numberOne * numberTwo}.")
    case '/':
        if(numberTwo == 0):
            print("Cannot divide by zero.")
        else:
            print(f"The result is {numberOne / numberTwo}.")