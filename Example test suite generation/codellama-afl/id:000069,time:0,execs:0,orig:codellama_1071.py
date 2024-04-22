# Using as() to convert a string to an integer
str = "123"
int_val = int(str)
print(int_val) # Output: 123

# Using filter() to remove all odd numbers from a list of integers
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(odd_numbers) # Output: [2, 4, 6]