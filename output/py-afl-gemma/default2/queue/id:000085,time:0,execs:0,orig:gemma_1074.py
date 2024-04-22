
async def hello_world():
    print("Hello, world!")

# Use as and await
async with open("test.txt") as f:
    await hello_world()

    # Read data from the file
    data = await f.read()

    # Print the data
    print(data)
