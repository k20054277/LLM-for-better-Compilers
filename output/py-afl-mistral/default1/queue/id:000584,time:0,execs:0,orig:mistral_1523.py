
# A simple function to validate if a given key exists in the dictionary and its value is a number.
def valid_input(data, expected_key, expected_value):
    assert data is not None, "Error: Data is None"
    assert isinstance(data, dict), "Error: Data is not a dictionary"
    assert expected_key in data, f"Error: Key '{expected_key}' not found in the data."
    assert isinstance(data[expected_key], (int, float)), f"Error: Expected value of key '{expected_key}' to be a number."
    print(f"Key '{expected_key}' has value {data[expected_key]} which is of type {type(data[expected_key])}.")
    
# Sample data
my_data = {"name": "John", "age": 30, "city": "New York"}

# Test the function with given key and expected value in the dictionary
valid_input(my_data, "age", 35)

# Test the function with key that doesn't exist in the dictionary
try:
    valid_input(my_data, "color", "red")
except AssertionError as e:
    print("Assertion failed:", e)
