
def even_numbers(n):
    """Yields even numbers from 1 to n."""
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

# Use the even_numbers function to generate even numbers
even_numbers_iterator = even_numbers(10)

# Iterate over the even numbers
for number in even_numbers_iterator:
    print(number)
