
import socket

def main():
    host = '127.0.0.1'  # Standard loopback interface address (localhost)
    port = 12345        # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Server started at {host}:{port}")
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f'Connected by {addr}')
            while True:
                data = input("Enter a message or type 'q' to quit: ")
                if data == 'q':
                    break
                conn.sendall(data.encode())
                response = conn.recv(1024)
                print(f"Received from client: {response.decode()}")

if __name__ == "__main__":
    main()
