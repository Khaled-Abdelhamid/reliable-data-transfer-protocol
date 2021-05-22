from socket import *

serverName = "192.168.1.11"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input lowercase sentence:")
message = 'hello'
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("From Server:", modifiedMessage.decode())
clientSocket.close()
