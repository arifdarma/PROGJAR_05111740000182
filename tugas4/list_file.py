import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("list ")
    request = command.encode()
    print(request)
    sock.send(request)
    data = sock.recv(1024)
    print("list file:")
    print(data.decode())
finally:
    print("closing")
    sock.close()
