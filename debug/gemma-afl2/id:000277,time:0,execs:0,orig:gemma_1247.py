
# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Use the as keyword to bind the variable even to the result of the function call
even = is_even(8)

# Assert that even is True
assert even

# Print the value of even
print(even)
