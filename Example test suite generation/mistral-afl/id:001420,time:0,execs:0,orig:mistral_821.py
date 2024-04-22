
def filter_even_numbers(numbers):
    """Generator function to filter out even numbers between 2 and 5"""
    for num in numbers:
        if num > 1 and num % 2 == 0:  # Filter condition using 'and' operator
            yield num

# Test the generator function
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_numbers = filter_even_numbers(numbers)

print("Filtered even numbers:")
for num in filtered_numbers:
    print(num)
