
def even_numbers(n):
    """Yields even numbers from 1 to n."""

    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i


# Create an instance of the even_numbers generator
even_numbers_gen = even_numbers(10)

# Iterate over the generator and print each element
for number in even_numbers_gen:
    print(number)
