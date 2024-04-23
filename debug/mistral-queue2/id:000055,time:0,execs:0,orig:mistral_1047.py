
# Let's assume we have a list of strings, each containing two integers separated by a space
data = ["1 2", "3 4", "5 6", "7 8"]

# Using a generator expression with 'as' and 'for':
square_generator = (int(num)**2 for string in data for num in string.split() if int(num) > 0 as sq)

# Now we can iterate through this generator using 'next()' function or for loop:
print("Square numbers greater than zero from input data:")
for _ in range(4): # Assuming we want to print four numbers
    print(next(square_generator))

print("\nList comprehension using 'as':")
# Using list comprehension with 'as' and 'for':
squares = [int(num)**2 for string in data for num in string.split() if int(num) > 0 if int(num)%2 == 0 as square]
print(squares)
