import socket #socket for ip and pc login
import getpass #getpass for username
print ("Hello ",getpass.getuser()) #take username
print ("Your login:",socket.gethostname()) #take login
print ("Your External IP:",socket.gethostbyname_ex(socket.gethostname())[-1][0]) #take external IP
#-- Old version (with connect website)--#
# import socket #socket for ip and pc login
# import getpass #getpass for username
# Ip = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #take ip and socket
# Ip.connect(("google.ru",80)) #test connect
# Ip_for_print= Ip.getsockname()
# print ("Hello ",getpass.getuser()) #take username
# print ("Your login:",socket.gethostname()) #take login
# print ("Your IP:",Ip_for_print[0]) #vivod Ip adressa
