import socket

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to a server on port 80 (HTTP)
server_address = ('www.example.com', 80)
sock.connect(server_address)

# send a GET request for the home page
sock.sendall(b'GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n')

# receive the response
response = sock.recv(4096)

# check if the response is valid
if response:
    # parse the response headers and body
    headers, body = response.split(b'\r\n\r\n', 1)
    print(headers)
    print(body)
else:
    print("No response received")

# close the socket
sock.close()