#The client programm that sends the information to the server

import socket

#Some constants (client ip, port)
CLIENT = socket.gethostbyname(socket.gethostname())
PORT = 55555
HOST_IP = '127.0.0.1'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST_IP, PORT))
client.send("Penis".encode('utf-8'))
