import socket
import select

HEADER_LENGTH = 50

IP = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## just opening the socket for the server.
#Af: address family, inet is just internet.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
# this line allows you to reconnect to the server without it saying that the address is in use

server_socket.bind((IP, PORT)) #binding the ip and the port to the socket so I can use it as a server.

server_socket.listen(2)  #the queue only takes 2 connections.

print("Server is running: \nWaiting for Connections...")


sockets_list = [server_socket] #since we already have the server socket as a socket, we put it here. 

clients = {} #this is just to be able to print the user names and stuff in a better way so we will have the socket as a key and the user data as a value.

def recv_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    except:
        return False
        
while True:
    read_sockets, dummy_, exception_sockets = select.select(sockets_list, [], sockets_list)
     #select takes in 3 parameters the "read" list and the "write" lists and the sockets we might error on.
    
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            print(client_socket, client_address)

            user = recv_message(client_socket)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user

            print(f"accepted new connection from {client_address}:{client_address[1]} username: {user['data'].decode('utf-8')}")
        else:
            message_ = recv_message(notified_socket)
            if message_ is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print(f"Recevied Message from {user['data'].decode('utf-8')}: {message_['data'].decode('utf-8')}")

            for client_socket in clients:
                if client_socket != notified_socket:
                    client_socket.send(user['header'] + user['data'] + message_['header'] + message_['data'])
                    
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]













