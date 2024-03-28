
import asyncio

class EchoClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reader = bytearray()

    async def connect(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        self.writer = writer
        return reader

    async def send(self, message):
        self.writer.write(message.encode())
        await self.writer.drain()

    async def receive(self):
        while True:
            data = await self.reader.read(1)
            if not data:
                break
            self.reader.append(data)
            print(f'Received byte: {data}')

    async def run(self):
        reader = await self.connect()
        await self.send(b'Hello, server!')
        await self.receive()
        await self.writer.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    client = EchoClient('localhost', 12345)
    try:
        await loop.run_until_complete(client.run())
    finally:
        loop.close()
