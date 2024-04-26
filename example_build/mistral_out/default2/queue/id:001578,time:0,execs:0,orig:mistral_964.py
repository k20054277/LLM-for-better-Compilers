
# Function to check if a number is positive
def is_positive(num):
    return num > 0

# Function to validate user input and perform division
def divide():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Check if both numbers are positive
        if is_positive(num1) and is_positive(num2):
            print(f"The result of {num1} divided by {num2} is {num1 / num2}")
        else:
            print("Error: Both numbers must be positive")
    except ValueError as e:
        print(f"Error: {e}")

# Calling the divide function
divide()
