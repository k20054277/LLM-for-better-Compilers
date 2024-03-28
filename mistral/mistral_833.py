
# Function that checks if a number is even and positive
def is_even_positive(num):
    return num > 0 and num % 2 == 0

# Test some numbers
numbers = [1, -3, 4, 7]
for num in numbers:
    print(f"Number {num} is even and positive: {'True' if is_even_positive(num) else 'False'}")
