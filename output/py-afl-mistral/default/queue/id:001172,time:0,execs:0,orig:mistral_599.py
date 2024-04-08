
# List of boolean values using True and False
booleans = [True, True, False, True, False]

# List of corresponding integers
numbers = [1, 2, 3, 4, 5]

# Using zip() to pair each boolean value with its corresponding integer
paired = zip(booleans, numbers)

# Printing the paired values using for loop
for pair in paired:
    print(f"Boolean Value: {pair[0]}")
    print(f"Corresponding Integer: {pair[1]}")
    print()
