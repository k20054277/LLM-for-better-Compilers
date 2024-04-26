
# This Python program demonstrates the use of and and elif statements.

# Define a function called check_age.
def check_age(age):
    # If the age is greater than 18, return True.
    if age > 18:
        return True
    # Otherwise, return False.
    elif age < 18:
        return False

# Get the user's age.
user_age = int(input("What is your age? "))

# Check if the user is eligible to vote.
if check_age(user_age):
    print("You are eligible to vote.")
elif check_age(user_age) is False:
    print("You are not eligible to vote.")
