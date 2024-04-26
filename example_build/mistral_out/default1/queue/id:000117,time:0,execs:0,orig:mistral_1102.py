
# List of tuples with two elements each
numbers_and_squares = [(2, 4), (3, 9), (5, 25)]

# Extracting and assigning lists using standard method
first_nums, squares = [], []
for num_square in numbers_and_sqares:
    first_nums.append(num_square[0])
    squares.append(num_square[1])

print("Using standard method:")
print("First numbers:", first_nums)
print("Squares:", squares)

# Using as keyword for assignment from iterable
first_nums, squares = [], []
for num_square in numbers_and_sqares:
    first_nums, squares = num_square

print("\nUsing 'as' keyword:")
print("First numbers:", first_nums)
print("Squares:", squares)
