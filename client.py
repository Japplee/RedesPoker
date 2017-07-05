import socket
import threading
import sys

HOST = 'localhost'
PORT = 8888

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def sendMsg():
    while True:
        client_socket.send(bytes(input(""), 'utf-8'))

client_socket.connect((HOST, PORT))
iThread = threading.Thread(target=sendMsg)
iThread.daemon = True
iThread.start()

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(data)

client_socket.close()