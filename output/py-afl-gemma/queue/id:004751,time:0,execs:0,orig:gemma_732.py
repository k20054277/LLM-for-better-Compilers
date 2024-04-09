
# Define a function to check if a number is even
def is_even(num):
  return num % 2 == 0

# Use the function to check if various numbers are even
print(is_even(4))  # Output: True
print(is_even(5))  # Output: False
print(is_even(6))  # Output: True

# True is used to check if the function returns True
if is_even(8):
  print("8 is even")  # Output: 8 is even
