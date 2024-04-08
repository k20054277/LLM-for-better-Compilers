
# server.py
import socket

def main():
    host = '127.0.0.1'
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Listening on {host}:{port}")

    connection, client_address = server_socket.accept()
    try:
        message = "Hello, client! I'm a truthy value."
        connection.sendall(message.encode())
    finally:
        connection.close()
        server_socket.close()

if __name__ == "__main__":
    main()
