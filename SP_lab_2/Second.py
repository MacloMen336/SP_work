import socket #podkluchenie biblioteki socket 
import os
##Ip = socket.gethostbyname(socket.gethostname()) #v peremennyu Ip polychaem Ip adress
#Ip = socket.gethostbyname('lo')
Ip = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Ip = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_Ip_socket = '192.168.15.1'
#Ip.connect(("google.ru",80))
if (Ip.connect((serv_Ip_socket,20))<0):
	puts('Connect Fail')
print ("Your login:",socket.gethostname())
print ("Your IP:",Ip.getsockname()) #vivod Ip adressa
message = "Hello Lev"


if (send(Ip,message,strlen(message),0)<0):
	puts('message Connect Failed')
#print ("hello")

