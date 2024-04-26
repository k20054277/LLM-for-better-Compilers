# Demonstrating the use of None and in

# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use None to represent an empty slot in the list
numbers.append(None)

# Print the contents of the list with None values
print("List:", numbers)

# Check if a value is in the list using in
if 2 in numbers:
    print("Value 2 is in the list.")
else:
    print("Value 2 is not in the list.")

# Check if a value is None using is
if None in numbers:
    print("None is in the list.")
else:
    print("None is not in the list.")