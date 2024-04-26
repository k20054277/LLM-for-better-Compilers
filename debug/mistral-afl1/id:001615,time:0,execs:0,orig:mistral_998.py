
# Example program to demonstrate the usage of 'and' and '*' operators in Python

def main():
    # Defining variables
    num1 = 5
    num2 = 3

    # Using 'and' operator for conditional statements
    print("Condition 1:")
    if (num1 > 0) and (num2 > 0):
        print(f"Both {num1} and {num2} are positive numbers.")

    print("\nCondition 2:")
    if (num1 > 0) and (num2 < 0):
        print("Number 1 is positive, but Number 2 is negative.")

    # Using '*' operator for multiplication
    print("\nMultiplication:")
    result = num1 * num2
    print(f"The product of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
