
# Set initial condition as False
is_adult = False

# Get user's age using input() function
user_age = int(input("Please enter your age: "))

# Check if user is an adult based on their age
if user_age >= 18:
    is_adult = True
    print("Welcome, you are an adult!")
else:
    print("Sorry, you are not old enough to enter.")

# Loop continues with True statement
while is_adult:
    # Add any other logic or processing here if needed
    print("You are considered an adult in our system.")
