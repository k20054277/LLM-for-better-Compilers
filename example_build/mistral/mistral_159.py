
# Set some variables
number = -5
minimum_age = 18

# Use conditional statements to check some conditions
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative and less than zero.")

# Check if a number is valid for voting
age = 15

if age >= minimum_age:
    print(f"You are old enough to vote.")
elif age > 0:
    print(f"You are not old enough to vote, but you are above zero.")
else:
    print("Invalid input. Age should be a positive number.")
