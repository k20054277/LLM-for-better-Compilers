
# This Python program demonstrates the use of AND and SUM operations

# Define a function to demonstrate AND and SUM operations
def demonstrate_and_sum(num1, num2):
    # Use the AND operator to check if num1 and num2 are both greater than 5
    if num1 > 5 and num2 > 5:
        # Sum the two numbers and print the result
        print("The sum of num1 and num2 is:", num1 + num2)

# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the function to demonstrate AND and SUM operations
demonstrate_and_sum(num1, num2)
