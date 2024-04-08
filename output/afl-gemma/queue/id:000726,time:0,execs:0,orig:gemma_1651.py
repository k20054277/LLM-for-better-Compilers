
import asyncio

async def hello_world():
    print("Hello, world!")

asyncio.run(hello_world())

# The above program prints "Hello, world!" to the console

# You can also use str to print a string
async def print_string(string):
    print(string)

asyncio.run(print_string("Hello, world!"))

# This will also print "Hello, world!" to the console
