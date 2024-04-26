
import socket

# Define a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
sock.bind((localhost, 8080))

# Listen for connections
conn, addr = sock.listen()

# Accept a connection
print("Client connected: ", addr)

# Send a message to the client
message = "Hello, world!"
conn.sendall(message.encode())

# Receive a message from the client
data = conn.recv(1024).decode()

# Print the client's message
print("Client message:", data)

# Close the connection
conn.close()

# Close the socket
sock.close()
