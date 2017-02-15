# TP1

## Compte GIThub
hihi

## Client UDP Python
Le programme est dans le chapitre 2 du livre que nous étudions.

* Récupérer le PDF sur le drive 
* Chercher la page
* Copier le programme dans un éditeur de code
* Executer

````python 
#!/usr/bin/python
from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input("Depeche de donner une phrase jai  pas ton temps:")
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()

#!/usr/bin/python
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "Quand tu veux mon poto ca fonctionne de ouf"
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)


```
ke
