
# Define a function that takes an integer as an argument and returns its absolute value using abs() function
def get_absolute_value(num):
    return abs(num)

# Define a function that checks if a number is positive or zero, using and keyword
def is_positive(num):
    return (num > 0) and (num is not None)

# Take user input as a number
number = int(input("Enter a number: "))

# Check if the number is positive using is_positive function and print the result
if is_positive(number):
    print(f"The given number {number} is positive.")
else:
    # If the number is not positive, get its absolute value using get_absolute_value function and print the result
    print(f"The given number {number} is not positive. Its absolute value is:")
    print(get_absolute_value(number))
