
import socket

def handle_client(client_socket):
    message = client_socket.recv(1024).decode()
    assert message == b"Hello from client", "Unexpected message from client"
    response = "Hello Server!"
    client_socket.sendall(response.encode())
    client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")
    server_socket.listen()

    while True:
        client_socket, _ = server_socket.accept()
        handle_client(client_socket)
