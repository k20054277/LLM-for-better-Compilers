
# Server.py
import socket

def start_server():
    host = ''
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    try:
        s.bind((host, port))
    except socket.error as msg:
        print('Bind failed. Error Code :' + str(msg[0]) + ' Message :' + msg[1])
        sys.exit()

    print("Socket bind complete")
    print("Listening on", host, ":", port)
    s.listen(3)

    conn, addr = s.accept()
    print('Connected by', addr[0],':',addr[1])
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        response = "True"
        conn.sendall(response.encode())
        
    print('Closed connection')
    s.close()

if __name__ == "__main__":
    start_server()
