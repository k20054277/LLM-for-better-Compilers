
# Import required modules
import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 5000        # Arbitrary non-used port number

    server_socket = socket.socket()   # Create a socket object
    server_socket.bind((host, port))  # Bind the socket to the address and port

    print("Waiting for connection from client...")
    server_socket.listen(1)          # Start listening for the client connection
    conn, addr = server_socket.accept()  # Establish the connection with the client

    print(f"Connection from {addr} has been established.")

    password = "secretpassword".encode('ascii')
    msg = "Hello Client".encode('ascii')

    while True:
        data = conn.recv(1024)   # Receive data from client

        if data and data == password:  # Check condition for the correct password
            conn.sendall(msg)         # Send greeting message to the client
        else:
            print("Incorrect password sent by the client.")

    conn.close()              # Close the connection
    server_socket.close()      # Close the socket

if __name__ == "__main__":
    start_server()
