# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use True to check if a number is in the list
if True in numbers:
    print("Yes, 1 is in the list.")
else:
    print("No, 1 is not in the list.")

# Delete an element from the list using del
del numbers[0]
print(numbers)  # Output: [2, 3, 4, 5]