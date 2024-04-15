
# This is a simple Python script that demonstrates the usage of 'and' operator and 'import' statement

# Importing the math module for mathematical operations
import math

# Define a function 'is_positive_number' that checks if given number is positive
def is_positive_number(n):
    return n > 0

# Define another function 'is_even_number' that checks if given number is even
def is_even_number(n):
    return n % 2 == 0

# Function to get user input and process the conditions
def main():
    try:
        num = int(input("Enter a number: "))

        # Using 'and' operator for multiple conditions in if statement
        if is_positive_number(num) and is_even_number(num):
            print(f"The number {num} is positive and even.")
            
        elif is_positive_number(num):
            print(f"The number {num} is positive.")
            
        else:
            print("Invalid input. Please enter a valid positive or negative integer.")

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
