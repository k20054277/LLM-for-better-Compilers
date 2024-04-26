
# This Python program demonstrates the use of and and <= operators

# Define a function to check if a number is greater than 5 and less than or equal to 10

def check_number(num):
  return num > 5 and num <= 10

# Get the number from the user

number = int(input("Enter a number: "))

# Check if the number meets the conditions

if check_number(number):
  print("The number", number, "is greater than 5 and less than or equal to 10.")
else:
  print("The number", number, "does not meet the conditions.")
