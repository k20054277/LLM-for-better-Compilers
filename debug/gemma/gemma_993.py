
# This Python program demonstrates the use of and and debugging

# Define a function called "check_condition"
def check_condition(num1, num2):
    # Use an and condition to check if num1 is greater than 5 and num2 is less than 10
    if num1 > 5 and num2 < 10:
        print("Both conditions are true")
    else:
        print("One or both conditions are false")

# Get two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Call the "check_condition" function
check_condition(num1, num2)

# Print the result
print("The result is:", num1, "and", num2)
