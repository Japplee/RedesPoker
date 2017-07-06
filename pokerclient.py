import socket
import threading
import sys
import pickle
from player import Player

nombre = raw_input("Ingrese nombre: ")
PLAYER = Player(nombre, 1000)
HOST = 'localhost'
PORT = 8888

csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

csocket.connect((HOST, PORT))

while True:
    data = csocket.recv(1024)

    if data == "sendhand":
        newhand = pickle.loads(csocket.recv(1024))
        PLAYER.hand = newhand
        print PLAYER.showHand()

    if not data:
        break

    print(data)

csocket.close()