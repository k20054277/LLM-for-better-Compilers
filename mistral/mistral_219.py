
# Define a dictionary with some keys and values
data = {1: 'one', 2: 'two', 3: 'three'}

# Set a variable to False
is_finished = False

# Function that checks if a key exists in the dictionary and prints its value
def get_value(dct, key):
    if key in dct:
        value = dct[key]
        print(f"The value for the key {key} is: {value}")
        return True
    else:
        print(f"The key {key} does not exist in the dictionary.")
        return False

# Use double unpacking to assign multiple values from a tuple to variables
x, y = (1, 2)
print(f"x is {x} and y is {y}")

# Call the function with dictionary and key as arguments
get_value(data, 1)  # This will print: The value for the key 1 is: one
get_value(data, 4)  # This will print: The key 4 does not exist in the dictionary.
