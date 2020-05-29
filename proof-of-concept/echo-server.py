import socket
import random
import time
import os

def play_game_server(f, client_socket):
    while True:
        my_number = str(random.randrange(1,2))
        print (my_number)
        f.write('my_number = ' + my_number)
        client_socket.sendall(my_number.encode())
        print('sent  ', my_number)


        data = client_socket.recv(1024)
        print('received ', data.decode())

        if not data:
            break;

        your_number = data.decode()
        f.write('your_number = ' + your_number)

        if your_number > my_number:
            f.write('Server Lost')
            break;

        if your_number < my_number:
            f.write('Server Won')
            break;

        client_socket.sendall('again'.encode())
        print('again!')
        data = client_socket.recv(1024)
        print('received ', data.decode())

time.sleep(random.randrange(0,3))

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

client_socket, addr = server_socket.accept()
f.write('Connected by' + str(addr))

f.write('GAME ' + GAME_NUMBER + ' started')
play_game_server(f, client_socket)
f.write('GAME ' + GAME_NUMBER + ' finished')


# 받은 문자열을 다시 클라이언트로 전송해줍니다.(에코) 
client_socket.sendall('game finished'.encode())


client_socket.close()
server_socket.close()

f.close();



