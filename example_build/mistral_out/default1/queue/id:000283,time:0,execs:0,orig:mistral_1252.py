
# Assigning a value to a variable using alias
x = 5
y = x as new_name
print(x) # Output: 5
print(y) # Output: 5

# Renaming list elements
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first) # Output: 1
print(last) # Output: 5
print(middle) # Output: [2, 3]
