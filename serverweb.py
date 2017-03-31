from socket import *
serverPort = 8080
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept()
	req = connectionSocket.recv(1024)
	mot = req.split(" ")
	oui = mot[1]
	oui = oui[1:]
	f=open(oui,"r+t")
	connectionSocket.send(f.read())
	connectionSocket.close()