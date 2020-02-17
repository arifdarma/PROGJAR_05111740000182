import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 30000)
host = socket.gethostname()
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    with open('recieved_file', 'wb') as f:
        while True:
            # data = connection.recv(64)
            data = connection.recv(1024)
            if not data:
                break
            f.write(data)
    f.close()
    # Clean up the connection
    connection.close()
