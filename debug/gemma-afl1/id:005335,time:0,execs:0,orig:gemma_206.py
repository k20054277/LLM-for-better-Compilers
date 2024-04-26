
# This Python program demonstrates the use of the and and input functions.

# Get the user's name and age.
name = input("What is your name? ")
age = int(input("How old are you? "))

# Check if the user is eligible to vote.
eligible = (age >= 18) and (name != "John Doe")

# Print the results.
if eligible:
  print("You are eligible to vote.")
else:
  print("You are not eligible to vote.")
