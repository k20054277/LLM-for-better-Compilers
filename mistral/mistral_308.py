
# Define a function that returns None if given list is empty
def empty_list(input_list):
 if len(input_list) > 0:
 return input_list
 else:
 return None

# Define a function that returns a frozenset of unique elements from given list
def to_frozenset(input_list):
 return frozenset(input_list)

# Define a sample list
my_list = [1, 2, 3, 3, 4, 5, 5]

# Call functions with my_list as an argument and print results
print("Empty list check: ", empty_list(my_list))
print("Frozenset creation: ")
frozen_set = to_frozenset(my_list)
print(frozen_set)
