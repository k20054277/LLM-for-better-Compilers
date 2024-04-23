
def number_generator(limit):
    num = 0
    while num < limit:
        yield num
        num += 1

# Generate sequence up to 5
numbers = number_generator(5)
next(numbers) # Get the first item (0)
