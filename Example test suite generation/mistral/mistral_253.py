
# A function that checks if a number is positive or if it is None
def is_positive(num):
    if num is not None:
        return num > 0
    else:
        print("Number is None")
        return None

# A list of numbers
numbers = [1, 2, 3, 4, 5]

# Check each number in the list and print the result
for num in numbers:
    result = is_positive(num)
    if result is not None:
        print(f"Number {num} is positive: {result}")
    else:
        print(f"Number {num} is not positive and is also None")

# Check for a nonexistent key in a dictionary
my_dict = {"key1": 1, "key2": 2}
nonexistent_key = "key3"
result = my_dict.get(nonexistent_key)
if result is None:
    print(f"{nonexistent_key} does not exist in the dictionary")
else:
    print("An error occurred, nonexistent key should be None")

# Demonstrating and operator
a = 5
b = 10
c = 15

# Check if a is positive and b is greater than c
if a > 0 and b > c:
    print("Both conditions are met")
else:
    print("One or both of the conditions is not met")
