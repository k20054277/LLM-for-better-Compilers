
# A simple list
numbers = [1, 2, 3, 4, 5]

# Using enumerate() to get index-value pairs
for index, number in enumerate(numbers, start=1):
    print(f"Index: {index}, Value: {number}")

# Now let's use 'as' for better readability when unpacking the tuple returned by enumerate()
for index_value in (index, value) in enumerate(numbers, start=1):
    index, value = index_value
    print(f"Index: {index}, Value: {value}")
