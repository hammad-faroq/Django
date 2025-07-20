import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#cleint will first create an endpint connected to the scoket
mysock.connect(('data.pr4e.org', 80))#client will first start commnuication
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()

