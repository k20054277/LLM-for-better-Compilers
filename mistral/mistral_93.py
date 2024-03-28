
# Define a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using False as the slice step to get all elements except for every second element
odd_numbers = my_list[::-2 if False else 1]

print("List with every second number removed: ", odd_numbers)

# Using slicing to extract a portion of the list
start = 0
stop = 3
step = 1
slice_part = my_list[start:stop:step]

print("First three elements: ", slice_part)
