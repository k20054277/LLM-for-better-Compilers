
# Initializing a list called numbers
numbers = [10, 20, 30, 40, 50]

# Printing the initial state of the list
print("Initial State of List:")
print(numbers)

# Removing an element from the list using del keyword
index_to_remove = 2
del numbers[index_to_remove]

# Printing the updated state of the list
print("\nUpdated State of List after deletion:")
print(numbers)

# Using True to check if an element is present or not in the list
element_to_check = 40
if 40 in numbers:
    print(f"\nThe element {element_to_check} is present in the updated list.")
else:
    print(f"\nThe element {element_to_check} is not present in the updated list.")

# Using True to check if an empty list or tuple is empty
my_list = []
my_tuple = ()

print("\nChecking if lists and tuples are empty using True:")
print(f"\nList is empty? {bool(my_list)}")
print(f"\nTuple is empty? {bool(my_tuple)}")
