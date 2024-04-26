
# This function checks if a given number is positive, and prints its square if it is
def print_square_if_positive(number):
 if number > 0:
 print(number ** 2)
 else:
 print("Number is not positive")

# Using for loop to iterate over a list of numbers
numbers = [1, -3, 4, -5, 7]
for num in numbers:
 if True:  # This condition always evaluates to True
 print_square_if_positive(num)
