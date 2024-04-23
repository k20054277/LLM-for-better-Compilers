
# Python Program for Demonstrating True and Division Operator (/)

def main():
    # Taking input numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Performing division operation
    result = num1 / num2

    # Checking if the result is greater than zero using Boolean value True
    if result > 0:
        print(f"The result {result} is positive.")
        print("Therefore, the following statement will be true:")
        print(True)
    else:
        print(f"The result {result} is non-positive.")
        print("Therefore, the following statement will be false:")
        print(False)

if __name__ == "__main__":
    main()
