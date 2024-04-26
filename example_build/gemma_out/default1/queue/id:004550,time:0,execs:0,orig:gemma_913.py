
# This Python program demonstrates the use of and and slice

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use and to filter out numbers divisible by 2
 divisible_by_2 = [x for x in numbers if x % 2 == 0]

# Slice the list of numbers from the beginning to the fifth element
fifth_elements = numbers[:5]

# Print the results
print("Numbers divisible by 2:")
print( divisible_by_2)

print("Fifth elements of the list:")
print(fifth_elements)
