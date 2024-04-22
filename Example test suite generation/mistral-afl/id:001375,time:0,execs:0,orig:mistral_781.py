
# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Set a variable with a boolean value
is_even = True

# Check if an element is present in the list and its value is even
if is_even and 0 in (numbers[i] % 2 for i in range(len(numbers))):
    print("An even number is present in the list")
else:
    print("No even number is present or 'is_even' is False")
