
# server.py
import socket

def start_server():
    host = '127.0.0.1'
    port = 5000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print('Waiting for connection...')
        conn, addr = s.accept()
        print(f'Connected by {addr}')

        with conn as c:
            request = c.recv(1024).decode()
            print(f'Received request:\n{request}\n')
            response = 'Hello from server!'
            c.sendall(response.encode())
            print('Sent response:', response)

if __name__ == '__main__':
    start_server()
