
# First condition: check if a number is even
def is_even(num):
 return num % 2 == 0

# Second condition: check if a number is greater than zero
def is_positive(num):
 return num > 0

# Function using and keyword to check if a number is positive and even
def is_positive_and_even(num):
 result = is_even(num)
 result = result and is_positive(num)
 return result

# Testing the function with some numbers
print(is_positive_and_even(4)) # True
print(is_positive_and_even(-1)) # False
print(is_positive_and_even(0)) # True
