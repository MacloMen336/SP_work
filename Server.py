import socket

HOST = '192.168.0.17'  # needed interface address
PORT = 9090       # Port to listen on (non-privileged ports are > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) #bind need port
    s.listen() #listen port and work if some go in port
    conn, addr = s.accept() #take address who connect
    with conn:
        print('Connected by', addr) #print address who connect
        while True:
            data = conn.recv(1024) #check on connect
            if not data:
                break
            print(f'{addr[0]} send: ',str(data)[2:-1]) #print massege
            conn.sendall(bytes('i read your message', encoding = 'UTF-8')) #send message

#--code without answer--#     
# import socket
# HOST = '192.168.0.17'  # Standard loopback interface address (localhost)
# PORT = 9090       # Port to listen on (non-privileged ports are > 1023)
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             print(str(data)[2:-1])
			