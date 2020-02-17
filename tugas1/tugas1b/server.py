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
    filename = connection.recv(32)
    try:
        f = open(filename, 'rb')
    except:
        print("Cannot open file")
    else:
        length = f.read(1024)
        while length:
            connection.send(length)
            length = f.read(1024)
    f.close()
    # Clean up the connection
    connection.close()
