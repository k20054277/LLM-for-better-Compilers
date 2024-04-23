
def is_number(n):
    """Function to check if an element is a number"""
    return isinstance(n, (int, float))

def double_numbers(nums):
    """Function to double each number in a given list"""
    return [num * 2 for num in nums]

nums = ['1', '2', 3, 4, '5', 6]

# Using assert for type checking and validation
assert all(map(is_number, nums)), "Input list contains non-numeric elements"

# Using filter() to remove non-numeric elements from the list
nums_filtered = list(filter(is_number, nums))

print("Original List: ", nums)
print("Filtered List: ", nums_filtered)

nums_doubled = double_numbers(nums_filtered)

print("Doubled Numbers: ", nums_doubled)
