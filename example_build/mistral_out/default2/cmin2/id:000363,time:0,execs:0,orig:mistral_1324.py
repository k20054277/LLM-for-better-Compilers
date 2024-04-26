
def validate_dict(input_dict):
    # Keys and expected values
    keys_and_values = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Validate input dictionary with given keys and expected values using assert statement
    for key, value in keys_and_values.items():
        assert key in input_dict, f"Key '{key}' is missing in the input dict."
        assert input_dict[key] == value, f"Value of key '{key}' is not as expected."
        
# Test the validate_dict function with a valid dictionary
test_dict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
validate_dict(test_dict)
print("Test passed!")

# Test the validate_dict function with an invalid dictionary
invalid_dict = {
    "name": "John Doe",
    "age": 31,
    "city": "New York"
}
try:
    validate_dict(invalid_dict)
except AssertionError as error:
    print(f"Test failed! Error: {error}")
