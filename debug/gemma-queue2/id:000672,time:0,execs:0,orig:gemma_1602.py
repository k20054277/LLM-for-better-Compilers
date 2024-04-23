
import asyncio

async def hello_world():
    print("Hello, world!")

# Compile the function into a bytecode object
compiled_hello_world = asyncio.compile(hello_world)

# Run the compiled function asynchronously
await compiled_hello_world()

print("Done!")
