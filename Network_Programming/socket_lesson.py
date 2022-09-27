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
# import socket 
# mysock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org',80))
# cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# while True:
#     data=mysock.recv(512)
#     if (len(data)<1):
#         break
#     print(data.decode())
# mysock.close()


'''
http request using urllib
'''

# import urllib.request, urllib.parse,urllib.error
# fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())



'''
like a file
'''

# import urllib.request, urllib.parse,urllib.error
# fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# count=dict()

# for line in fhand:
#     words=line.decode().split()
#     for word in words:
#         # print(word)
#         count[word]=count.get(word,0)+1
# print(count)

'''
reading web pages
'''

import urllib.request, urllib.parse,urllib.error
fhand=urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())


# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# for line in fhand:
#     print(line.decode().strip())


