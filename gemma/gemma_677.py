
# This Python program demonstrates the use of True and sorted

# Create a list of numbers
numbers = [1, 3, 5, 2, 4, 6]

# Check if the list is sorted in ascending order
is_sorted = numbers is sorted()

# If the list is sorted, print True
if is_sorted:
    print("The list is sorted in ascending order.")

# Sort the list in ascending order
numbers.sort()

# Print the sorted list
print(numbers)

# Check if the list is sorted in ascending order after sorting
is_sorted_after_sort = numbers is sorted()

# If the list is sorted, print True
if is_sorted_after_sort:
    print("The list is sorted in ascending order after sorting.")
