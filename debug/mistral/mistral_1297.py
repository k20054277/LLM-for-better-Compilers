
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to check if a number is in the list
def check_number_in_list(num, lst):
    assert isinstance(lst, list), "The second argument must be a list"
    result = num in lst
    return result

# Test cases for the function
test_numbers = [1, 2, 3, 4, 5, 6]

# Test case 1: Number is in the list
print(check_number_in_list(5, numbers))  # Should print True

# Test case 2: Number is not in the list
print(check_number_in_list(6, numbers))  # Should print False

# Test case 3: List is not a list
try:
    check_number_in_list(5, test_numbers[::-1])
except AssertionError as e:
    print("Error:", e)
else:
    print("Test passed")
