import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Write IP address of Server: ')
ips = input () #input needed IP address
print ('Write Port of Server: ')
port = (int(input())) #input needed port
sock.connect((ips, port)) #try connect
while True:
    print ('Write the massage you want to send: ') 
    ms = input() #input what message you want send
    sock.send(bytes(ms, encoding = 'UTF-8')) #send message like bite
    data = sock.recv(1024) #wait answer
    print(f'Server give answer: ',str(data)[2:-1]) #print server answer

#--code without answer--#  
# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print ('Write IP address of Server: ')
# ips = input ()
# print ('Write Port of Server: ')
# port = (int(input()))
# sock.connect((ips, port))
# while True:
#     print ('Write the massage you want to send: ')
#     ms = input()
#     sock.send(bytes(ms, encoding = 'UTF-8'))