import socketio
import os
import socket
from time import sleep 
import threading


sio = socketio.Client()

sio.connect('http://130.89.6.69:8080')
sio.emit('sum', {'numbers': [1,3]})

import select
import sys
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "130.89.6.69"
Port = 8082
server.connect((IP_address, Port))
 

@sio.event
def connect():
    print("I'm connected!")

@sio.event
def connect_error(data):
    print("The connection failed!")

@sio.event
def disconnect():
    print("I'm disconnected!")

@sio.event
def sum_result(data):
    print (data)
    

@sio.event
def feedback(data):
    print(data)
    #print(str(data["id"]) + " - " + data["feedback"])
    server.send(data['feedback'].encode())
    #if robotServerStarted == False:
    #    start()

@sio.event
def feedbackResponse(data):
    sio.emit('feedbackResponse', {'responseFromRobot': data})


while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            #print (message)
            feedbackResponse(message)
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
server.close()

