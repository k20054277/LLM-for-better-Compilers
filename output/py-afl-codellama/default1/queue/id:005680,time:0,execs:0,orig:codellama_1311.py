# Ask the user for their name
name = input("What is your name? ")

# Use assert to check if the name is not empty
assert name != "", "Name cannot be empty"

print(f"Hello, {name}!")