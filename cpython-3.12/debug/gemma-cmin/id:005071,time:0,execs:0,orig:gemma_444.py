
# This Python program demonstrates the use of False and debugging

# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Check if 6 is even
is_even(6)  # Output: True

# Check if 5 is even
is_even(5)  # Output: False

# Debug the function
print(is_even(5))  # Output: False

# The function is not working because it's checking if the remainder when num is divided by 2 is 0, which is true for even numbers, but not for 5.
# To fix the function, we need to change the condition to check if the remainder when num is divided by 2 is 0. Here's the corrected function:

def is_even(num):
  return num % 2 == 0

# Check if 6 is even
is_even(6)  # Output: True

# Check if 5 is even
is_even(5)  # Output: False

# Now, the function is working correctly
print(is_even(5))  # Output: False
