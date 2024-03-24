
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Filter function that checks if number is even
def is_even(number):
    return number % 2 == 0

# Iterator from filter function and list
iter_filtered = filter(is_even, numbers)

# Using 'and' to check conditions
print("Even numbers using 'and':")
try:
    even_number = next(iter_filtered)
    print(next(iter_filtered) if even_number and even_number > 0 else None)
except StopIteration:
    print("No even number greater than zero.")

# Using 'and' to combine conditions in a for loop
print("\nEven numbers using 'and' in for loop:")
for number in filter(lambda x: x % 2 == 0 and x > 0, numbers):
    print(number)
