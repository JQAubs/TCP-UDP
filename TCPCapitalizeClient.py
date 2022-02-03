import socket
import time
import random

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket for the client
host = str(input('input host name: '))
port = int(input('Please enter a port number...\n'))  # connect client to same port

message_times = []

if host == 'l':
    host = 'localhost'
# connect to the host
ClientSocket.connect((host,port))      # establish connection to the host

print("handshake: ", ClientSocket.recv(1024).decode('UTF-8', 'strict'))
print('type \'exit\' at any time to close the program.')
transmitting = True
number_transmissions = 1

while transmitting:

    message = ''
    while len(message) <= 0:
        message = str(input("Message #%i: " % number_transmissions))
        if message == '':
            print('That is not valid...')

    if message == 'exit':
        transmitting = False
        message = 'UEXIT'
        ClientSocket.send(message.encode())
        break

    MessageStartTime = time.time()
    ClientSocket.send(message.encode())

    try:
        response = ClientSocket.recv(1024).decode('UTF-8', 'strict')
        MessageEndTime = time.time()
    except:
        print('The server disconnected')

    if 'SEXIT' in response:
        print('The server disconnected')
        break

    else:
        print('Recieved: %s' % response)
        print('response took %f seconds in total.' % (MessageEndTime-MessageStartTime))
        message_times.append(MessageEndTime-MessageStartTime)
        number_transmissions += 1


print('Networking stats:')
print('Average Transmission time: %f seconds.'% (sum(message_times)/len(message_times)))
print('there were %i transmissions in total.' % len(message_times))
print('total transmission time %f seconds.' % sum(message_times))

ClientSocket.close()
