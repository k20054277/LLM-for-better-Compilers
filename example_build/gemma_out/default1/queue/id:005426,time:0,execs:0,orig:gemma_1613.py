
import asyncio

async def hello_world():
    print("Hello, world!")

asyncio.run(hello_world())

print(format("The message is: %s", "async"))
