
# List creation
numbers = [1, 2, 3, 4, 5]

# Assertion: Check if all elements in the list are positive numbers
def assert_positive_numbers(num_list):
    for num in num_list:
        assert num > 0, f"Negative number found: {num}"

assert_positive_numbers(numbers)

# Slicing: Extract a portion of the list
start = 2
end = 4
slice_numbers = numbers[start:end]

print("Original List: ", numbers)
print("Sliced List:  ", slice_numbers)
