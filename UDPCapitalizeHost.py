import socket
import random
import time

def printHostInfo(host, port):
    info = socket.getaddrinfo(host, port)
    print('UDP Local: ', str(info[0]))
    print('TCP Local: ', str(info[1]))
    #print('UDP Public: ', str(info[2]))
    #print('TCP Public: ', str(info[3]))

def serverLifetimeElapsed(start, now, limit):
    return (now - start) < limit

host = str(input('Please enter the host name...\n'))
port = int(input('Please enter a port number...\n'))

if host == 'l':
    host = 'localhost'

printHostInfo(host, port)

HostSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HostSocket.bind((host, port)) # bind the hostname/port number to the socket

StartTime = time.time()
timeLimit = 800
Server_Open = True

while Server_Open:

    Server_Open = serverLifetimeElapsed(StartTime, time.time(), timeLimit)

    message, addy = HostSocket.recvfrom(1024)
    print('recieved: ', message)

    HostSocket.sendto(message.upper(), addy)


HostSocket.close()
