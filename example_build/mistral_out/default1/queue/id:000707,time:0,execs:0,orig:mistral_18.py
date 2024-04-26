
# This function checks if a given number is even or not
def check_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

# List of numbers to check
numbers = [1, 2, 3, 4, 5, 6]

# Using for loop and boolean value False
for num in numbers:
  if not check_even(num):
    print(f"{num} is odd")
