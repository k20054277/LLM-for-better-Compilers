
import asyncio

class EchoServer:
    async def __aenter__(self):
        self.reader, self.writer = await asyncio.open_connection('localhost', 1234)
        return self
    
    async def echo(self, message):
        self.writer.write(message.encode())
        await self.writer.drain()
        response = ''
        data = []
        while True:
            chunk = await self.reader.read(1)
            if not chunk:
                break
            data.append(chunk)
            response += chunk.decode()
        return response.strip()
    
    async def __aexit__(self, exc_type, exc, tb):
        self.writer.close()
        await self.writer.wait_closed()

async def main():
    with EchoServer() as server:
        message = 'Hello World!'
        response = await server.echo(message)
        print(f'Received: {response}')

if __name__ == '__main__':
    asyncio.run(main())
