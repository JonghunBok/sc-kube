import socket
import random
import time
import os

def play_game_server(f, client_socket):
    while True:
        server_number = str(random.randrange(1,10))
        print (server_number)
        f.write('server_number = ' + server_number + '\n')
        client_socket.sendall(server_number.encode())
        print('sent  ', server_number)


        data = client_socket.recv(1024)
        print('received ', data.decode())

        if not data:
            break;

        client_number = data.decode()
        f.write('client_number = ' + client_number + '\n')

        if client_number > server_number:
            f.write('Server Lost' + '\n')
            break;

        if client_number < server_number:
            f.write('Server Won' + '\n')
            break;

        client_socket.sendall('again'.encode())
        print('again!')
        data = client_socket.recv(1024)
        print('received ', data.decode())


HOST = ''
PORT = 9999        


if not os.path.exists('/tmp/games'):
    os.makedirs('/tmp/games')

GAME_NUMBER = os.environ['GAME']
f = open("/tmp/games/log_server_" + GAME_NUMBER + ".txt", 'w')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()

f.write('-------------------------------------------\n')

client_socket, addr = server_socket.accept()
f.write('Connected by' + str(addr) + '\n')

f.write('GAME ' + GAME_NUMBER + ' Server\'s log.\n')
play_game_server(f, client_socket)
f.write('GAME ' + GAME_NUMBER + ' Server\'s log finished' + '\n')


# 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코) 
client_socket.sendall('game finished'.encode())


client_socket.close()
server_socket.close()

f.close();



