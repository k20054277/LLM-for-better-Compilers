
# Define a function called 'is_even' to check if a number is even
def is_even(n):
  return n % 2 == 0

# Use the as keyword to bind the variable 'even_number' to the result of calling the 'is_even' function with the number 10 as an argument
even_number = is_even(10)

# Test if the variable 'even_number' is equal to True
if even_number:
  print("The number 10 is even")

# Output
# The number 10 is even
