
import socket
import unittest

# Define a test case class
class TestSocket(unittest.TestCase):

    def setUp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def tearDown(self):
        self.sock.close()

    def test_connection(self):
        self.sock.connect(('localhost', 8080))
        assert self.sock.isconnected() is True

    def test_send_and_receive(self):
        self.sock.send(b'Hello, world!')
        received_data = self.sock.recv(1024)
        assert received_data.decode() == 'Hello, world!'

if __name__ == '__main__':
    unittest.main()
