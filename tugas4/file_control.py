import shelve
import uuid
import socket
import os
import base64

class File:
    def __init__(self):
        if not os.path.exists("files"):
            os.makedirs("files")

    def upload_file(self,nama=None,isi=None):
        data_file = isi
        f = open("files/"+nama,"wb")
        f.write(base64.b64decode(data_file))
        return True

    def download_file(self,nama=None):
        temp = []
        f = open("files/" + nama, "rb")
        l = f.read()
        f.close()
        hasil = base64.b64encode(l)
        temp.append(hasil.decode())
        return temp

    def list_files(self):
        file_list = os.listdir("files")
        f = []
        for filename in file_list:
            f.append(filename)
        return f

if __name__=='__main__':
    f = File()