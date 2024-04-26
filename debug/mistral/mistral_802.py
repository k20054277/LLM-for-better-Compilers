
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Perform division, checking for zero as denominator with 'and'
    result = num1 / num2
    if num2 != 0:  # Alternatively, this condition can be put inside try block
        print(f"Result: {result}")
    else:
        print("Error! Division by zero is not allowed.")

except ValueError as ve:
    print(f"Error occurred: {ve}")
