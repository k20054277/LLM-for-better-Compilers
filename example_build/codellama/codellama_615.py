# Ask the user for their age
age = int(input("What is your age? "))

# Check if the user is over 18
if age >= 18:
    print("You are old enough to enter.")
elif age < 18 and age > 0:
    print("You are not old enough to enter.")
else:
    print("Invalid input. Please enter a positive integer.")