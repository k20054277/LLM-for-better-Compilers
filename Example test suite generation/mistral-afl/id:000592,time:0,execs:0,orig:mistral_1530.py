
import asyncio

async def handle_client(reader, writer):
    data = ""
    while True:
        line = await reader.readline()
        if not line:
            break
        data += line.decode('utf-8').rstrip()
        print("Received data:", data)
        await writer.write(b'Received Data\n')
        await writer.drain()
    print("Client disconnected")
    await writer.close()

async def asynchronous_server(host: str, port: int):
    server = await asyncio.start_server(lambda r, w: handle_client(r, w), host, port)
    print(f"Serving on {host}:{port}")
    async with server:
        await asyncio.serve_forever(server)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        await asynchronous_server("127.0.0.1", 8888)
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
