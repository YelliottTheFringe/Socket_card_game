import socket as sk
import sys as s
# initilize a game server
    # get the technical stuff out of the way.
def cprin(message):
    for i in message:
        s.stdout.write(i)

def send(message,clients,socket):
    if type(clients) == list:
        for i in clients:
            socket.send(message.encode())
    else:
        socket.send(message.encode())
    
# rounds
def round1():
    pass # round 1
def round2():
    pass
def round3():
    pass

# MAIN
def svmain():
    game = True
    PORT = int(input("Port? "))
    sock = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
    sock.bind(('',PORT))
    sock.listen(4)
    clients=[]
    while game:
        sv_connect_and_comunicate(sock)
    sock.close()

    
def sv_connect_and_comunicate(socket):
    client, addr =socket.accept()
    print(client,addr)

svmain()
