num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op == "+":
    result = num1 + num2
    print("Result =", result)
elif op == "-":
    result = num1 - num2
    print("Result =", result)
elif op == "*":
    result = num1 * num2
    print("Result =", result)
elif op == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
        result = None
    else:
        result = num1 / num2
        print("Result =", result)
else:
    print("Invalid operator")
    result = None
if result is not None:
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")
