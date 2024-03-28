# Using None and iter() to iterate over an iterator

my_list = ['a', 'b', 'c']

# Create an iterator object from the list
iterator = iter(my_list)

# Use the has_next() method of the iterator to check if there are more elements in the iterator
while iterator.has_next():
    # Print the next element in the iterator
    print(iterator.next())

# Using None to represent a missing value

# Create a dictionary with a missing value
d = {'a': 1, 'b': 2, 'c': None}

# Use None as a value in a list comprehension
new_list = [v for v in d.values() if v is not None]

print(new_list)  # Output: [1, 2]