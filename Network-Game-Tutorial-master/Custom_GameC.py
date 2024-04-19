import socket as sk
from time import sleep
coord=(12,50)
def waitfor(signal):
    brk=True
    while brk:
        if sock.recv(1024).decode() == signal:
            print("the game begins")
            break
        else:
            sleep(0.001)
def move():
    pass
def dataParserR(data): #cut the data recieved from the server into the two coordinates. (recv)
    pass
def dataParserS(data): #(send)
    message=''
    message+=str(data[0])+"n"+str(data[1])
    return message
sock=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
sock.connect(('127.0.0.1',12002))
waitfor('000')
game=True
while game:
    print((dataParserS(coord)))
    sock.send(dataParserS(coord).encode())
    sock.recv(1024)
