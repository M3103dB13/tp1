from socket import *
passattendu = "hey"
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024) 
	capitalizedSentence = sentence.upper()
	print (capitalizedSentence)
	serverSocket2 = socket(AF_INET,SOCK_STREAM)
	serverSocket2.bind(("",13000))
	serverSocket2.listen(1)
	print "The server is ready to send"
	while 1 :
		connectionSocket2, addr = serverSocket2.accept()
		modSentence = connectionSocket2.recv(1024)
		print (modSentence)
		if modSentence == passattendu :
			connectionSocket2.send(capitalizedSentence)
			connectionSocket2.close()
		if modSentence != passattendu :  
			connectionSocket2.send("MDP Faux")
			connectionSocket2.close()