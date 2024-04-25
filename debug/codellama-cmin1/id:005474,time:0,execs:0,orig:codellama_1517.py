import asyncio

async def main():
    data = b'Hello, world!'
    buffer = await asyncio.create_buffer(data)
    print(buffer)
    # Output: <asyncio.BufferProtocol object at 0x1037d84e0>
    print(buffer.getvalue())
    # Output: b'Hello, world!'
    buffer.close()

asyncio.run(main())