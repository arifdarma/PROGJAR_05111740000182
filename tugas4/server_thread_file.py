from socket import *
import socket
import threading
import logging
import time
import sys
import base64

from file_machine import FileMachine

fm = FileMachine()

class ProcessTheClient(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        temp = (b"")
        test = []
        while True:
            while True:
                data = self.connection.recv(1024)

                temp = temp + data
                test.append(data)
                size = int(sys.getsizeof(data))

                if size != 1057 :
                    break
                else :
                    self.connection.sendall(b"OK")
            data = temp

            if data:
                d = data.decode()
                hasil = fm.proses(d)
                print(hasil)
                self.connection.sendall(hasil.encode())
            else:
                break
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.the_clients = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind(('0.0.0.0', 5000))
        self.my_socket.listen(1)
        while True:
            self.connection, self.client_address = self.my_socket.accept()
            logging.warning(f"connection from {self.client_address}")

            clt = ProcessTheClient(self.connection, self.client_address)
            clt.start()
            self.the_clients.append(clt)


def main():
    svr = Server()
    svr.start()


if __name__ == "__main__":
    main()
