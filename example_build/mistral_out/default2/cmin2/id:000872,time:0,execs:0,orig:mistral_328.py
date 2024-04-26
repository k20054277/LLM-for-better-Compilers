
# Define an empty list
my_list = []

# Use None to represent a missing value
missing_value = None

# Function that returns the next number from a list
def next_number(numbers):
    if len(numbers) > 0:
        return next(numbers)
    else:
        print("No more numbers in the list.")
        return missing_value

# Define a list of numbers and iterate through it using next_number()
numbers = [1, 2, 3, 4]
current = next_number(numbers)
print(current) # Output: 1
current = next_number(numbers)
print(current) # Output: 2

# Try to get the next number from an empty list
current = next_number(my_list)
print(current) # Output: None

# Define a dictionary and use next() to iterate through its keys
my_dict = {"apple": 1, "banana": 2, "cherry": 3}
keys = iter(my_dict.keys())
key = next(keys)
print(key) # Output: 'apple'
key = next(keys)
print(key) # Output: 'banana'
key = next(keys)
print(key) # Output: 'cherry'
key = next(keys) # Raises a StopIteration exception
