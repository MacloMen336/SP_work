import socket #podkluchenie biblioteki socket 
Ip = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #take ip and socket
Ip.connect(("google.ru",80)) #test connect
Ip_for_print= Ip.getsockname()
print ("Your login:",socket.gethostname()) #take login
print ("Your IP:",Ip_for_print[0]) #vivod Ip adressa






