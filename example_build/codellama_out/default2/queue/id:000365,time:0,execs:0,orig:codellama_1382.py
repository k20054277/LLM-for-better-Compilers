import socket

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

print('Server listening on {}'.format(server_address))

while True:
    # Wait for a connection
    connection, address = sock.accept()
    try:
        # Receive the data from the client
        data = connection.recv(1024)
        
        # Print the received data
        print('Received {} bytes from {}: {}'.format(len(data), address, data))
        
        # Send a response back to the client
        connection.sendall(b'Hello, world!')
    finally:
        # Clean up the connection
        connection.close()