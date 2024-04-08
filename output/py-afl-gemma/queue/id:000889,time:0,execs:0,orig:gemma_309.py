
# This Python program demonstrates the use of False and any

# Define a list of elements
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Check if any element in the list is False
if any(False in elements):
    print("There is a False element in the list.")

# Check if all elements in the list are True
if all(True in elements):
    print("All elements in the list are True.")

# Check if the list is empty
if not elements:
    print("The list is empty.")
