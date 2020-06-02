import socket
import random
import os
import time

def play_game_client(f, client_socket):
    while True:
        data = client_socket.recv(1024)
        server_number = data.decode()
        f.write('server_number = ' + server_number + '\n')

        client_server = str(random.randrange(1,10))
        print (client_server)
        f.write('client_server = ' + client_server + '\n')
        client_socket.sendall(client_server.encode())
        print('sent  ', client_server)


        data = client_socket.recv(1024)
        print('received ', data.decode())

        if not data:
            break;
        
        if data.decode() == 'game finished':
            break;
        
        client_socket.sendall('okay'.encode())

        f.write('server says ' + data.decode() + '\n')

        

time.sleep(random.randrange(0,3))

HOST = ''  
PORT = 9999       

if not os.path.exists('/tmp/games'):
    os.makedirs('/tmp/games')

GAME_NUMBER = os.environ['GAME']
f = open("/tmp/games/log_client_" + GAME_NUMBER + ".txt", 'w')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while client_socket.connect_ex((HOST, PORT)) != 0:
    time.sleep(1)


f.write('-------------------------------------------\n')
f.write('GAME ' + GAME_NUMBER + ' Client\'s log.' + '\n')
play_game_client(f, client_socket)
f.write('GAME ' + GAME_NUMBER + ' Client\'s log finished' + '\n')

client_socket.close()
f.close()

