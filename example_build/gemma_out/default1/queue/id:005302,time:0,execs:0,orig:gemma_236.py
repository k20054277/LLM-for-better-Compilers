
# This Python program demonstrates the use of and and sum operators

# Define a function to demonstrate the use of and and sum operators
def demonstrate_and_sum(a, b):
    # Use the and operator to check if a and b are both greater than 5
    if a > 5 and b > 5:
        # Sum the two numbers and print the result
        print(a + b)

# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function to demonstrate the use of and and sum operators
demonstrate_and_sum(num1, num2)
