
import socket

def main():
    # Try to connect to a server using a given IP address and port number.
    ip_address = "127.0.0.1"
    port_number = 80

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to the server using the given IP address and port number.
            sock.connect((ip_address, port_number))

            print("Connected to the server.")

            # Send a message to the server and receive a response.
            message = "Hello, server!".encode('utf-8')
            sock.sendall(message)

            response = sock.recv(1024).decode('utf-8')

            print("Received response from the server:", response)

    except OSError as err:
        if err.errno == 10061:
            print("Error connecting to the server:", str(err))
            print("The server is probably not running or is unreachable.")
        else:
            raise

    elif socket.has_ipv6():
        print("IPv6 is available on this system.")

    else:
        print("Unable to connect to the server.")

if __name__ == "__main__":
    main()
