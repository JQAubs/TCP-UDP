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
printHostInfo(host, port)

HostSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HostSocket.bind((host, port)) # bind the hostname/port number to the socket
HostSocket.listen(2) # wait for a connection to the client

StartTime = time.time()
timeLimit = 800
Server_Open = True

while Server_Open:

    Connection, addr = HostSocket.accept() # establish connection with client
    print("client %s has connected to the server..."% str(addr))
    greeting = 'Type a message... \n'
    Connection.send(greeting.encode('UTF-8', 'strict'))

    talking = True
    while talking:

        Server_Open = serverLifetimeElapsed(StartTime, time.time(), timeLimit)

        if not Server_Open:
            Connection.send('SEXIT'.encode('UTF-8','strict'))
            break

        r = Connection.recv(1024).decode('UTF-8', 'strict')
        print('recieved: ', r)

        if 'UEXIT' == r:
            print('client session concluded...')
            break

        Connection.send(r.upper().encode('UTF-8', 'strict'))

    Connection.close()

    Server_Open = serverLifetimeElapsed(StartTime, time.time(), timeLimit)

HostSocket.close()
