
# Example using as with list comprehension and a generator expression
import itertools

# Using 'as' for naming items in a list comprehension
numbers = [x * 2 for x in range(10) as i]  # i is an optional name for the index variable
print("List Comprehension: ", numbers)

# Using 'as' for renaming items in a generator expression
generator = (x ** 2 for x in range(5) if x % 2 == 0 as square_number)
print("Generator Expression: ")
print([next(generator) for _ in range(3)])

# Example using 'or' operator
def is_even(n):
    return n % 2 == 0

def is_multiple_of_three(n):
    return n % 3 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Numbers: ", numbers)
even_or_multiple_of_three = lambda x: is_even(x) or is_multiple_of_three(x)
print("Even or multiple of three: ", [x for x in numbers if even_or_multiple_of_three(x)])
