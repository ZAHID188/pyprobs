'''
socket understanding :
a software structure within a network node of a computer network that
serves as an endpoint for sending and receiving data across the network. 
'''

# import socket 
# mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect( ('data.pr4e.org',80) )

'''
http request using socket
'''
import socket 
mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data=mysock.recv(512)
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
