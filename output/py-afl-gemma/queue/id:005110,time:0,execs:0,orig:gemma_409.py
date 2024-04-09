
import socket

# Define a false boolean value
is_true = False

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
sock.bind((localhost, 8080))

# Listen for connections
while True:
    # Accept a connection
    conn, addr = sock.accept()

    # Send a message to the client
    conn.sendall(b"Hello, world!")

    # Close the connection
    conn.close()

# Close the socket
sock.close()
