
def sum_list(numbers):
    # Assert if input is a list
    assert isinstance(numbers, list), "Input should be a list"

    # Calculate the sum of elements in the list
    total = sum(numbers)

    # Use an assert statement to check if total is greater than or equal to zero
    assert total >= 0, f"Sum of list elements should not be negative. Sum: {total}"

    return total

# Test cases
print("Test case 1:", sum_list([1, 2, 3]))
print("Test case 2:", sum_list([-1, -2, -3])) # This test should raise an AssertionError
print("Test case 3:", sum_list([0, 0, 0]))
print("Test case 4:", sum_list([4.5, 6.2, 7.8])) # This test should raise a TypeError (as lists don't support float elements)
