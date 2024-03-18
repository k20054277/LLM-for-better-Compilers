
# False and zip demonstration program

# Create a list of False values
false_values = [False, False, False, False]

# Create a list of numbers
numbers = [1, 2, 3, 4]

# Zip the false values and numbers together
zipped = zip(false_values, numbers)

# Print the zipped items
for false, number in zipped:
    print(false, number)
