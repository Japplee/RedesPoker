import socket
import threading
import sys

HOST = 'localhost'
PORT = 8888

csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

csocket.connect((HOST, PORT))

while True:
    data = csocket.recv(1024)
    if not data:
        break
    print(data)

csocket.close()