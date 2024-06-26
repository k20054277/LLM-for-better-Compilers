
# True and iter

# True is a boolean value that evaluates to True or False
print(True)  # Output: True

# iter is a built-in function that iterates over an object
my_list = [1, 2, 3, 4, 5]
for num in iter(my_list):
    print(num)  # Output: 1 2 3 4 5

# You can also use True and iter to create a generator object
def my_generator():
    yield True
    yield False

for is_true in my_generator():
    print(is_true)  # Output: True False
