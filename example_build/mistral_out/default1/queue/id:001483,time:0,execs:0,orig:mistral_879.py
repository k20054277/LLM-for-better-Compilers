
# Define a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use and keyword for condition check
if (len(numbers) > 5) and (numbers[0] % 2 == 0):
    print("The list has more than 5 elements and the first element is even")
else:
    print("The conditions are not met")

# Use slicing to extract a subset of the list
start_index = 3
end_index = len(numbers)
sublist = numbers[start_index: end_index]
print("Sublist: ", sublist)
