# Demonstrate the use of True and min in Python

# Import the min function from the math module
from math import min

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the min function to find the minimum value in the list
min_value = min(numbers)

# Print the minimum value
print("The minimum value in the list is:", min_value)

# Use a conditional statement to check if the minimum value is less than 3
if min_value < 3:
    print("The minimum value is less than 3")
else:
    print("The minimum value is not less than 3")