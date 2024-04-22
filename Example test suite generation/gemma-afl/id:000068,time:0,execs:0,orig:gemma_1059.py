
# This Python program demonstrates the use of and and

# Define a function called "check_conditions" that checks two conditions
def check_conditions(num1, num2):
    # Use the and operator to check if both conditions are true
    return num1 > 10 and num2 < 20

# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the conditions are true
if check_conditions(num1, num2):
    # If the conditions are true, print a message
    print("The conditions are true")
else:
    # If the conditions are not true, print an error message
    print("The conditions are not true")
