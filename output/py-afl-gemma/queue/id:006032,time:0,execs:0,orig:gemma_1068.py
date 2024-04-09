
# This Python program demonstrates the use of and and []

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the and operator to check if all numbers in the list are greater than 2
all_greater_than_2 = (numbers[0] > 2) and (numbers[1] > 2) and (numbers[2] > 2) and (numbers[3] > 2) and (numbers[4] > 2)

# Print the result
if all_greater_than_2:
    print("All numbers in the list are greater than 2")
else:
    print("Not all numbers in the list are greater than 2")

# Use the [] operator to extract a sublist of numbers from the original list
sublist = numbers[1:3]

# Print the sublist
print(sublist)
