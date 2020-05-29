import socket
import random
import os
import time

def play_game_client(f, client_socket):
    while True:
        data = client_socket.recv(1024)
        your_number = data.decode()
        f.write('your_number = ' + your_number)

        my_number = str(random.randrange(1,3))
        print (my_number)
        f.write('my_number = ' + my_number)
        client_socket.sendall(my_number.encode())
        print('sent  ', my_number)


        data = client_socket.recv(1024)
        print('received ', data.decode())

        if not data:
            break;
        
        if data.decode() == 'game finished':
            break;
        
        client_socket.sendall('okay'.encode())

        f.write('server says ' + data.decode())

        

time.sleep(random.randrange(0,3))

HOST = ''  
PORT = 9999       

if not os.path.exists('/tmp/games'):
    os.makedirs('/tmp/games')

GAME_NUMBER = os.environ['GAME']
f = open("/tmp/games/log_client_" + GAME_NUMBER + ".txt", 'w')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

f.write('GAME ' + GAME_NUMBER + ' started')
play_game_client(f, client_socket)
f.write('GAME ' + GAME_NUMBER + ' finished')

client_socket.close()
f.close()

