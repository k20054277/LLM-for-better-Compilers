
# Initialize a list with some elements
numbers = [1, 2, 3, 4, 5]

# Iterate through the list while its length is greater than zero
while len(numbers) > 0:
    # Get the first element in the list
    current_number = numbers[0]

    print(f"Current number: {current_number}")

    # If the current number is not equal to False, remove it from the list
    if current_number is not False:
        del numbers[0]

# After the loop finishes, numbers will be an empty list
print("List is now empty: ", numbers)
