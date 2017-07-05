import socket
import threading
import sys
 
HOST = '' 
PORT = 8888 
CLIENTS_LIST = []
RECV_BUFFER = 1024
MAX_PLAYERS = 5
 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
    server_socket.bind((HOST, PORT))
except socket.error as msg :
    print 'Bind failed. Error Code: ' + str(msg[0]) + 'Message ' + msg[1]
    sys.ext()
print 'Socket bind complete'
server_socket.listen(MAX_PLAYERS)
print 'Socket now listening'

def handler(c, a):
    while True:
        data = c.recv(1024)
        for client in CLIENTS_LIST:
            client.send(data)
            if not data:
                break

while True :
    c, a = server_socket.accept()
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    CLIENTS_LIST.append(c)
    print(CLIENTS_LIST)