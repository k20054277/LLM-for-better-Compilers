
import itertools

def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares = map(square, even_numbers)

print("Even numbers and their squares:")
for i, (even, square) in enumerate(itertools.zip(even_numbers, squares)):
    print(f"{even} -> {square}")

print("\nNext even number:")
next_even = next(filter(lambda x: x % 2 == 0, itertools.count(1)))
print(next_even)
