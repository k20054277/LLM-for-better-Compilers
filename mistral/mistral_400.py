
# Define a list with some elements and some None values
my_list = [1, 2, 3, None, 5, None, 7, 8, None]

print("Original List:")
print(my_list)

# Iterate through the list using a for loop
print("\nIterating through the list:")
for element in my_list:
    if element is not None:
        print(element)
