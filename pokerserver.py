import socket
import threading
import sys
from deck import Deck
from player import Player
import random
 
HOST = '' 
PORT = 8888 
SOCKET_LIST = []
PLAYER_LIST = []
RECV_BUFFER = 1024
MAX_PLAYERS = 3
DECK = Deck()
SHUFFLE_TIMES = 3
DECK_POSITION = 51

def broadcast(msg): 
    for sock in SOCKET_LIST:
        sock.send(msg)

def shuffleCards():
    print 'Barajando cartas...'
    for i in range(SHUFFLE_TIMES):
        random.shuffle(DECK)
    print 'Mazo barajado ' + str(SHUFFLE_TIMES) + ' veces'

ssocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
try:
    ssocket.bind((HOST, PORT))
except socket.error as msg :
    print 'Bind failed. Error Code: ' + str(msg[0]) + 'Message ' + msg[1]
    sys.ext()
print 'Socket bind complete'
ssocket.listen(MAX_PLAYERS)
print 'Socket now listening'

for i in range(MAX_PLAYERS):
    print 'Esperando jugador ' + str(i) + "\n"
    conn, addr = ssocket.accept()
    SOCKET_LIST.append(conn)
    player = Player("Darby", 1000)
    PLAYER_LIST.append(player)
    print 'Se ha conectado jugador ' + str(i) + "\n"
    broadcast(str(i+1) + " de " + str(MAX_PLAYERS) + " jugadores conectados\n")
print 'Todos los jugadores se an conectado'
broadcast("Todos los jugadores conectados, Iniciando partida...")
broadcast("OPEN THE GAME!")

#Pre Flop
shuffleCards()
for x in range(len(PLAYER_LIST)):
    print 'Sirviendo cartas a jugador ' + str(x+1)
    for j in range(2):
        PLAYER_LIST[x].addCardToHand(DECK[DECK_POSITION])
        DECK_POSITION -= 1

    PLAYER_LIST[x].showHand()
#Flop Round
print 'Flop round'
#Turn Round

#River Round