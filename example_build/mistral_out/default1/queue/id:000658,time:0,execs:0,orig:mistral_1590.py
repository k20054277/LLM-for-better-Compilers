
import asyncio

class EchoServer:
    def __init__(self):
        self.server = asyncio.start_server(lambda r, w: self._handle_client(r, w), 'localhost', 8000)

    async def _handle_client(self, reader, writer):
        data = b''
        while True:
            new_data = await reader.read(1024)
            if not new_data:
                break
            data += new_data
            print(f'Message Received: {len(data)} bytes')
        writer.sendall(data)
        writer.close()
        await writer.wait_closed()

if __name__ == '__main__':
    server = EchoServer()
    asyncio.run(server.server)
