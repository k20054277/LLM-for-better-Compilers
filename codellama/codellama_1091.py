# Using "as" to create an alias for a variable
x = 10
y = x
print(y) # Output: 10

x = 20
print(y) # Output: 10

# Using "map" to apply a function to each element of a list
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]