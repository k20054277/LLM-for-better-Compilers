
# Define a function that checks if a given number is positive or not
def is_positive(num):
  # Use a conditional statement to check if the number is greater than zero
  # If it is, return the True boolean value
  # Otherwise, return False and an error message
  if num > 0:
    return True
  else:
    print("Error: The given number is not positive.")
    return False

# Test the function with some numbers
num1 = 5
num2 = -3
num3 = 0

# Use the is_positive function and assignment operator to assign the result (True or False) to a variable
result1 = is_positive(num1)
result2 = is_positive(num2)
result3 = is_positive(num3)

# Print out the results for each number
print("The number {0} is positive: {1}" .format(num1, result1))
print("The number {0} is positive: {1}" .format(num2, result2))
print("The number {0} is positive: {1}" .format(num3, result3))
