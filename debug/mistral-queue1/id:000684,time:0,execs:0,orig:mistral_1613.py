
import asyncio

class EchoServer:
    def __init__(self, host='127.0.0.1', port=54321):
        self.host = host
        self.port = port

    @staticmethod
    async def start_server():
        print('Starting server...')
        server = await asyncio.start_server(lambda r, w: EchoServer.handle_client(r, w), EchoServer().host, EchoServer().port)
        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')
        async with server:
            await server.serve_forever()

    @staticmethod
    async def handle_client(reader, writer):
        print('New client connection!')
        while True:
            data = await reader.readline()
            if not data: break
            print(f'Received: {data.decode()}')
            writer.write(data)
            await writer.drain()
            writer.write(b'\n')
        print('Client disconnected.')
        writer.close()

async def main():
    await EchoServer.start_server()

if __name__ == '__main__':
    asyncio.run(main())
