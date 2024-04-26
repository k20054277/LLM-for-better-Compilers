
# This Python program demonstrates the use of assert and enumerate

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate over the list and assert each element is greater than 0
for i, num in enumerate(numbers):
    assert num > 0

    # Print the index and value of each element
    print(f"Index: {i}, Value: {num}")

# Print a success message
print("All elements in the list are greater than 0")
