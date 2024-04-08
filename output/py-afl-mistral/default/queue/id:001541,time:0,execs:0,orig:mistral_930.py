
# Define a dictionary with some key-value pairs
data = {1: "apple", 2: "banana", 3: "cherry"}

# Function to check if a given key exists in the dictionary and its value is "banana"
def check_key_value(d, key, expected_value):
 if key in d and d[key] == expected_value:
 print(f"Key {key} has the expected value {expected_value}")
 else:
 print(f"Key {key} does not exist or has a different value")

# Test the function with some keys and expected values
check_key_value(data, 1, "apple") # Should print: Key 1 has the expected value apple
check_key_value(data, 2, "banana") # Should print: Key 2 has the expected value banana
check_key_value(data, 4, "orange") # Should print: Key 4 does not exist or has a different value
