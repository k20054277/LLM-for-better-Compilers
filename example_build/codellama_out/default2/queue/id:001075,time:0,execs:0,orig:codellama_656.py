# Example using the built-in range() function and the 'filter' function

def is_even(n):
    return n % 2 == 0

numbers = range(1, 11)

print("Original numbers:", numbers)

filtered_numbers = filter(is_even, numbers)

print("Even numbers:", list(filtered_numbers))