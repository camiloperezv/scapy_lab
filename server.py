import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('0.0.0.0', 8888)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096) 
    print(address, ':', data)
    if data:
        sent = sock.sendto('OK\n', address)