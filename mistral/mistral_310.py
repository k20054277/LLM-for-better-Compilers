
# Simple Calculator Program using None and globals() in Python

def calculate():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            print("Invalid Operator!")
            return None

        # Setting a global variable using globals() with None as default value
        globals()["ans"] = result

        print(f"Result: {result}")
    except Exception as e:
        print(e)
    finally:
        calculate()  # Calling the function recursively to perform next calculation

calculate()
print("Answer of last calculation is: ", globals()["ans"])
