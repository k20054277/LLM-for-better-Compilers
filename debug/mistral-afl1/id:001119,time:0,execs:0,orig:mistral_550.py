
# This is a simple Python program that uses the 'enumerate()' function along with a loop, where a condition (True) is used to control the iteration.

# Define a list
numbers = [1, 2, 3, 4, 5]

# Use enumerate() to get the index and value of each element in the list
for index, value in enumerate(numbers):
    if value > 3:  # The condition (True) is met when the current number is greater than 3
        print(f"Index: {index}, Value: {value}")
