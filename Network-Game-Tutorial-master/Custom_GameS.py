import socket as sk
import pygame as p
def dataParserR(data): #Parse the received data into a tuple for the server in watch mode
    pass
def dataParserS(data): #Parse the outgoing data, both cordinates sandwiched together in strings.
    print(data)

    

sock = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
sock.bind(('',12002))
sock.listen(2)
game=True
con=[]
coordC=(0,0)
cliSockA, cliIPA = sock.accept()
print("Player 1 connected!")
cliSockB, cliIPB = sock.accept()
print("Player 2 connected! Game begins.")
cliSockA.send('000'.encode())
cliSockB.send('000'.encode())
while game:
    coordA = (cliSockA.recv(1024).decode())
    coordB = (cliSockB.recv(1024).decode())
    print(coordA)
    print(coordB)
    outCoordsA=coordC,coordB
    outCoordsB=coordC,coordA
    outCoordsA=dataParserS(outCoordsA)
    width=20
    height=60
    sock.close()
    break
