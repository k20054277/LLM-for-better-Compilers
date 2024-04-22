
# Importing a module with alias
import math as mth

# Now we can use 'mth' instead of 'math'
print(mth.sqrt(16))  # Output: 4.0

# Another example, using a list comprehension and a lambda function
import operator as op

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: op.sqrt(x), numbers))
print(squares)  # Output: [1.0, 4.0, 9.0, 16.0]
