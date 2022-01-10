import socket
import select
import sys
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "130.89.6.69"
Port = 8082
server.connect((IP_address, Port))
 
while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message)
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            print("message sent")
server.close()

