
def increase_counter(counter):
    """
    This function increments the given counter by 1.
    It uses assert statement to check if the input is of integer type,
    and compounds assignment operator (+=) to increment the counter value.
    """
    if isinstance(counter, int):  # Check if the given argument is an integer
        print("Counter is an integer.")
        counter += 1  # Increment the counter using compound assignment operator
        return counter
    else:
        print("Error! Counter should be an integer.")
        assert isinstance(counter, int), "Counter must be an integer!"
        counter = counter + 1  # Increment the counter using normal addition operation
        return counter

# Testing the function
print("Testing with an integer:")
num = 5
result = increase_counter(num)
assert result == num + 1, "Function should have returned the expected value."
print(f"Expected: {num+1}, Actual: {result}")

print("\nTesting with a non-integer:")
str_value = "Hello"
result = increase_counter(str_value)
assert result is None, "Function should return None when given a non-integer."
