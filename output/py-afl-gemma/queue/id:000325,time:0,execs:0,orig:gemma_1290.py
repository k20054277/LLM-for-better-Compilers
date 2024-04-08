
# This Python program demonstrates the use of as and > operators

# Define a function called greet
def greet(name):
  print("Hello, " + name + "!")

# Assign the return value of the greet function to a variable called message
message = greet("John")

# Print the message
print(message)

# Check if the message is greater than 10 characters
if len(message) > 10:
  print("The message is greater than 10 characters")
else:
  print("The message is less than or equal to 10 characters")
