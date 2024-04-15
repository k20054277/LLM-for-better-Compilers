
# Define an asynchronous function that yields a sequence of numbers
async def numbers():
    for i in range(10):
        yield i

# Create an asynchronous generator object
async_gen = numbers()

# Iterate over the generator object and print each element
for num in async_gen:
    print(num)
