
# A list of numbers
numbers = [5, 2, 8, 1, 9, 4]

# Using assert to check if a number is positive
def assert_number_is_positive(number):
    assert number > 0, "Error: Number should be positive."

# Printing and checking the minimum number in the list
print("The minimum number in the list is:")
min_number = min(numbers)
print(min_number)

# Applying assert function to each number in the list
for num in numbers:
    assert_number_is_positive(num)

print("All numbers in the list are positive.")
