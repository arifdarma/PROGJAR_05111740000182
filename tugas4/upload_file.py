import socket
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 5000)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    command = ("upload ")
    namafile = input("enter filename: ")
    try:
        f = open(namafile, 'rb')
    except:
        print("cannot open file")
    else:
        datafile = base64.b64encode(f.read())
        f.close()
        f = open("temp","wb")
        f.write(datafile)
        f.close()
        f = open("temp","rb")
        request = command.encode() + namafile.encode() + (b" ") + f.read(1024)
        print(request)
        while (request):
            sock.send(request)
            request = f.read(1024)
            response = sock.recv(1024)
        print(response)
        f.close()
        os.remove("temp")
finally:
    print("closing")
    sock.close()
