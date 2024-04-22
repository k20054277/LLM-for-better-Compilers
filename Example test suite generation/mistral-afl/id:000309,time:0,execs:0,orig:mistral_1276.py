
# Use of parentheses for grouping expressions
def square(num):
    return num * num

result = (square(5), square(6))
print("Square of 5 and 6:", result)

# Use of as keyword for aliasing
import math

value, root = math.isqrt(16), math.sqrt(16)

print("Value and Square Root:")
print(f"Value: {value}")
print(f"Square Root: {root}")
print(f"Value is the square of root: {value ** 2 == root}")

# Use of as keyword with a generator expression
def count_even_numbers(start, stop):
    for num in range(start, stop):
        if num % 2 == 0:
            yield num

even_numbers = (num for num in range(10) if num % 2 == 0)
print("First three even numbers from a generator:")
for i in as_sequence(next(even_numbers), next(even_numbers), next(even_numbers)):
    print(i)
