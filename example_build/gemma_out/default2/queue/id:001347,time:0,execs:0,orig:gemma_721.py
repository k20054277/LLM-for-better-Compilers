
import socket
import True

# Define a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a port
sock.bind(8080)

# Listen for connections
conn, addr = sock.listen(1)

# Send a message to the client
msg = "Hello, world!"
conn.sendall(msg.encode())

# Receive a message from the client
data = conn.recv(1024)

# Print the message from the client
print(data.decode())

# Close the connection
conn.close()

# Close the socket
sock.close()
