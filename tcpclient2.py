from socket import *
serverName = "localhost"
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#connectionSocket.send("send it")
message = raw_input("Input password:")
clientSocket.send(message)
modifiedSentence = clientSocket.recv(1024)
print "From Server:", modifiedSentence
clientSocket.close()