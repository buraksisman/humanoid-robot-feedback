import socketio
import socket
from time import sleep 
import threading

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
        '/': './public/'
    })



@sio.event
def sum (sid, data):
    print(sid,data)
    result = data["numbers"][0]+data["numbers"][1]
    sio.emit("sum_result", result, broadcast=True)
    

@sio.event
def comment(sid, data):
    print(sid, data)
    sio.emit("comment", "world");


@sio.event
def connect(sid, environ):
    print(sid, 'connected')


@sio.event
def disconnect(sid):
    print(sid, 'disconnected')

@sio.event
def receiveFeedback(sid,data):
    print(data)
   # jsonData = { "id":1, "feedback": data }
    sio.emit("feedback", data, broadcast=True, include_self=False)
    print(data["feedback"])
    #send(data["feedback"])
#    try:
#        send(data["feedback"])
#        print(data["feedback"])
#    except socket.error:
#        print( "connection lost... reconnecting" )
#       connected = False  
        
        
      
        
        #while not connected:  
            # attempt to reconnect, otherwise sleep for 2 seconds  
        #    try:  
        #        client.connect(ADDR)
        #        connected = True  
        #        print( "re-connection successful" )  
        #    except socket.error:  
        #        sleep( 2 )  
        
        # continue normal operations  

@sio.event
def feedbackResponse(sid,data):
    print(data)
    sio.emit("feedbackResponseApp", data, broadcast=True, include_self=False)

