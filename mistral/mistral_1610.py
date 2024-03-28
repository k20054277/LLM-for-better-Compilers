
import asyncio

class AsyncServer:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        self._server = None

    @asyncio.coroutine
    def start_server(self):
        print('Starting server...')
        self._server = yield from asyncio.start_server(lambda r, w: self._handle_client(r, w), self.host, self.port)

    @asyncio.coroutine
    def _handle_client(self, reader, writer):
        print('Handling client request...')
        data = yield from reader.readline()
        setattr(self, 'message', data.decode())
        print(f'Received message: {getattr(self, "message")}')
        yield from writer.sendall(b'Server received your message.')
        self._server.close_connection(writer)
        print('Client request handled.')

class AsyncClient:
    def __init__(self, host='127.0.0.1', port=8888):
        self.host = host
        self.port = port
        self._reader = None
        self._writer = None

    @asyncio.coroutine
    def connect_to_server(self):
        print('Connecting to server...')
        self._transport, self._client = yield from asyncio.wait_for(asyncio.get_event_loop().create_connection(lambda: self, self.host, self.port), timeout=5)
        self._reader = self._transport.reader
        self._writer = self._transport.writer

    @asyncio.coroutine
    def send_message(self, message):
        print('Sending message...')
        yield from self._writer.sendall(message.encode())

@asyncio.coroutine
def main():
    server = AsyncServer()
    server_task = asyncio.ensure_future(server.start_server())

    client = AsyncClient()
    client_task = asyncio.ensure_future(client.connect_to_server())

    done, _ = asyncio.wait([server_task, client_task], return_when=asyncio.FIRST_COMPLETED)
    if not done:
        await server_task

    server.shutdown()

    print('Sending message from client...')
    yield from client.send_message(b'Hello Server')

    done, _ = asyncio.wait([server_task, client_task], return_when=asyncio.ALL_COMPLETED)

if __name__ == '__main__':
    asyncio.run(main())
