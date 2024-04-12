import socket as sk
import sys as s
def connect():
    IP = input("IP: ")
    PORT = int(input("Port:"))
    sock = sk.socket(sk.AF_INET,sk.SOCK_STREAM)
    sock.connect((IP,PORT))
    print("We good!")
    sock.close()

if __name__ =="__main__":
    connect()