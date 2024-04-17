
import asyncio

class Client:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.name = None

    async def send(self, message):
        self.writer.write(message.encode())
        await self.writer.drain()

    async def recv(self):
        data = await self.reader.readline()
        return data.decode().strip()
