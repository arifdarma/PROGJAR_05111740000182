import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = input("PORT :")
# Connect the socket to the port where the server is listening
server_address = ('localhost', int(port))
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    filename = input("Masukkan nama file :")
    try:
        f = open(filename, 'rb')
    except:
        print("Cannot open file")
    else:
        length = f.read(1024)
        while length:
            sock.send(length)
            length = f.read(1024)
        f.close()
finally:
    print("Closing")
    sock.close()
