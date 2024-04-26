
def my_generator(start):
    if start < 0:
        yield False
        return

    for num in range(2, int(start**0.5) + 1):
        if start % num == 0:
            yield False
            break

    yield start

for prime in my_generator(13):
    print(prime)
