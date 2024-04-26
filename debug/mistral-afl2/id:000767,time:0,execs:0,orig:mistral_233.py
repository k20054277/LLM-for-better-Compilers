
# Define the lower and upper bounds of the range
lower_bound = 10
upper_bound = 20

# Take two numbers as input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Use logical AND (&) to check if both numbers are within the given range
if num1 <= upper_bound and num1 >= lower_bound and num2 <= upper_bound and num2 >= lower_bound:
    print(f"Both numbers {num1} and {num2} are within the given range.")
else:
    # If any of the conditions is False, then both conditions will be False as well
    print("At least one of the numbers is not within the given range.")
    
# You can also demonstrate the use of False directly
if False and (num1 <= upper_bound and num1 >= lower_bound and num2 <= upper_bound and num2 >= lower_bound):
    print("This code will never be executed as the first condition is already False.")
