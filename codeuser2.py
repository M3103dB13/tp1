#!/usr/bin/python
from socket import *

serverName = "localhost"
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Depeche de donner une phrase jai  pas ton temps:")
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
