
import socket

# Define the host and port numbers
host = "localhost"
port = 8080

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((host, port))

# Send a message to the server
message = "Hello, world!"
sock.sendall(message.encode())

# Receive a message from the server
received_message = sock.recv(1024).decode()

# Print the received message
print(received_message)

# Close the socket
sock.close()
