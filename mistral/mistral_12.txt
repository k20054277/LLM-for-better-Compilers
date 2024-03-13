
# Function definition
def is_even(number):
  # Check if number is even by using the modulo operator %
  # If the remainder is 0, then the number is even
  if number % 2 == 0:
    return True
  else:
    return False

# Testing the function
print(is_even(4))        # Should print: True
print(is_even(5))        # Should print: False
