# Ask for user input
name = input("What is your name? ")
age = int(input("How old are you? "))

# Check if user is under 18
if age < 18:
    print(f"Hello, {name}. You are not allowed to enter.")

# Check if user is over 21
elif age > 21:
    print(f"Hello, {name}. You are of legal age and can enter.")

# Otherwise, print a generic greeting
else:
    print(f"Hello, {name}. You are of legal age but under 18. Have fun!")