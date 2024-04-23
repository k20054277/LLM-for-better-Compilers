# Prompt the user for their age
age = input("How old are you? ")

# Check if the user's age is less than 18
if age < 18:
    print("Sorry, you must be at least 18 to enter this site.")
    exit()

# Check if the user's age is between 18 and 25 (inclusive)
elif age >= 18 and age <= 25:
    print("Welcome! You can enter this site.")
else:
    print("Sorry, you are not eligible to enter this site.")