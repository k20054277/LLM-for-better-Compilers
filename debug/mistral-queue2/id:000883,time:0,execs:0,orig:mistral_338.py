
# Creating a list
numbers = [1, 2, 3, 4, 5]
print("Original List: ", numbers)

# Setting an element to None
numbers[2] = None
print("List after setting an element to None: ", numbers)

# Regular iteration
for num in numbers:
    if num is not None:
        print(num)

# Reverse Iteration using reversed()
for num in reversed(numbers):
    if num is not None:
        print(num)
