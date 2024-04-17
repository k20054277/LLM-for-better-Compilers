
# Function to check if a number is within a given range
def in_range(number, start, end):
    """
    :param number: The number to check.
    :param start: The start of the range.
    :param end: The end of the range.
    :return: True if number is between start and end (inclusive), False otherwise.
    """
    assert start <= end, "Start of range must be less than or equal to end."
    return start <= number <= end

# Test cases for in_range function
print("Test cases for in_range function:")

test_cases = [
    (5, 1, 5, True),
    (5, 1, 4, False),
    (5, 6, 5, True),
    (5, 6, 7, False),
]

for test in test_cases:
    number = test[0]
    start = test[1]
    end = test[2]
    expected = test[3]
    
    result = in_range(number, start, end)
    
    assert result == expected, f"Expected {expected} for inputs: {number}, {start}, {end}"
    print(f"\tPassed: Input: {number}, Start: {start}, End: {end}. Result: {result}")
