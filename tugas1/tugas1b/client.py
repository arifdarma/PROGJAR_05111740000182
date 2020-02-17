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
    print("Send file :", filename)
    sock.sendall(filename.encode())
    with open('recieved_file','wb') as f:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            f.write(data)
    f.close()
finally:
    print("Closing")
    sock.close()
