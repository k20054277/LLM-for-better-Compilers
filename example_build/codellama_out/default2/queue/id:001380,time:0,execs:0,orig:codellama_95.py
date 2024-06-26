# Using "and" with a list comprehension
numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers) # [2, 4]

# Using "and" with a filter function
def is_even(n):
    return n % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(even_numbers) # [2, 4]