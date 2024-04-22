
def process_data(data):
    """
    This function processes a list of numbers and checks for errors.
    :param data: List of numbers
    :return: None
    """
    expected_values = [1, 2, 3, 4, 5]
    processed_data = []

    # Process each number in the list
    for index, num in enumerate(data):
        result = num * 2
        processed_data.append(result)

        # Assertion check
        assert num in expected_values, f"Error: Unexpected number {num} found in data!"

    print("Processed data:", processed_data)

# Test the function with a list of numbers
data = [1, 2, 3, 4, 5]
process_data(data)

# Test the function with an unexpected number
data = [1, 2, 3, 4, 6]
try:
    process_data(data)
except AssertionError as e:
    print("Error:", e)
