#The server programm that takes the information from the client.


import socket

#Some constants (server ip, port)
SERVER = ''
PORT = 55555
ADDR = (SERVER, PORT)

#Socket initialization
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen(5)

#Accept a connection. The socket must be bound to an address and listening for connections.
#The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection,
#and address is the address bound to the socket on the other end of the connection.
while True:
    conn, address = server.accept()
    print(f"Connected to {address}.")
    message = conn.recv(2048).decode('utf-8')
    print(f"{message}")
