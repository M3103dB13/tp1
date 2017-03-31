from socket import *
serverName = "www.lycee-juleshaag.fr"
serverPort = 80
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = "GET / HTTP/1.1 \n\n\n\n"
clientSocket.send(message)
answer = clientSocket.recv(1024)
print "From Server:", answer
clientSocket.close()