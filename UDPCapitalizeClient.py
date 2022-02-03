import socket
import time
import random

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # create a socket for the client
host = str(input('input host name: '))
port = int(input('Please enter a port number...\n'))  # connect client to same port

message_times = []

if host == 'l':
    host = 'localhost'

curAddy = (host, port)

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
        break

    MessageStartTime = time.time()
    ClientSocket.sendto(message.encode(), curAddy)


    response, curAddy = ClientSocket.recvfrom(1024)
    MessageEndTime = time.time()
    response = response.decode('UTF-8', 'strict')
    
    print('Recieved: %s' % response)
    print('response took %f seconds in total.' % (MessageEndTime-MessageStartTime))
    message_times.append(MessageEndTime-MessageStartTime)
    number_transmissions += 1


print('Networking stats:')
print('Average Transmission time: %f seconds.'% (sum(message_times)/len(message_times)))
print('there were %i transmissions in total.' % len(message_times))
print('total transmission time %f seconds.' % sum(message_times))

ClientSocket.close()
