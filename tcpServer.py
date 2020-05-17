import socket
import select
import ast


HEADER_LENGTH = 10

# IP = "10.52.3.25"
IP = "127.0.0.1"
# IP = '25.135.227.60'
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




def recv_message(client_socket, metadata):
    # try:
        message_header = client_socket.recv(HEADER_LENGTH)
    
        if 'filep:' in message_header.decode('utf-8'):
            dataList = []
            meta = ast.literal_eval(metadata)
            data_size = sum([x[1] for x in meta])
            data = client_socket.recv(1000)
            while data_size > 0:

                data = client_socket.recv(1000)
                print(data_size, data)
                dataList.append(data)
                data_size -= len(data)

            print("Done Receiving.")
            return ('$fileData$', dataList)
            return False
        if '$ou#+' in message_header.decode('utf-8'):
            return ('sound', message_header)

        if '$acceptDd$' in message_header.decode('utf-8'):
            return ('accept', message_header)
        if '$cancelDd$' in message_header.decode('utf-8'):
             return ('cancel', message_header)
        if '$file$l#' in message_header.decode('utf-8'):
            fileLength = message_header.decode('utf-8').strip().split('#')[1]
            filename = client_socket.recv(int(fileLength))
            clean = client_socket.recv(10)
            f_c = (filename, clean)
            #metadata 
            lenPackets = client_socket.recv(10).decode().split('-')
            read = lenPackets[1]
            to_read = int(lenPackets[0]) - len(read) 
            metadata = client_socket.recv(to_read)
            metadata = read + metadata.decode()
            return ('file', message_header, f_c, metadata)

        if not len(message_header):
            return False
        message_length = int(message_header.decode("utf-8").strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}
    # except:
        # print('$' * 10)
        # return False
metadata = None
while True:
    read_sockets, dummy_, exception_sockets = select.select(sockets_list, [], sockets_list)
     #select takes in 3 parameters the "read" list and the "write" lists and the sockets we might error on.
    
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = recv_message(client_socket, metadata)
            if user is False:
                continue
            sockets_list.append(client_socket)
            clients[client_socket] = user
            print(f"accepted new connection from {client_address}:{client_address[1]} username: {user['data'].decode('utf-8')}")
        else:
            message_ = recv_message(notified_socket, metadata)
            soundMessage = False 
            fileNameTransfer = False
            fileTransfer = False
            acceptDownload = False
            cancelDownload = False
            
            if type(message_) == tuple and message_[0] == '$fileData$':
                fileTransfer = True
            elif type(message_) == tuple and message_[0] == 'sound':
                soundMessage = True
            elif type(message_) == tuple and message_[0] == 'file':
                metadata = message_[3]
                fileNameTransfer = True
            elif type(message_) == tuple and message_[0] == 'accept':
                acceptDownload = True
            elif type(message_) == tuple and message_[0] == 'cancel':
                cancelDownload = True
            elif message_ is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue
            user = clients[notified_socket]
            for client_socket in clients:
                if client_socket != notified_socket:
                    if soundMessage: 
                        client_socket.send(message_[1])
                    elif fileNameTransfer:
                        client_socket.send(message_[1] + message_[2][0])
                        client_socket.send(message_[2][1])
                        client_socket.send(f'{len(str(message_[3]))}-'.encode())
                        client_socket.send(f'{message_[3]}'.encode())
                    elif fileTransfer:
                        client_socket.send(message_[0].encode('utf-8'))
                        for pk in message_[1]:
                            client_socket.send(pk)
                    elif acceptDownload:
                        client_socket.send(message_[1])
                    elif cancelDownload:
                        client_socket.send(message_[1])
                    else:
                        client_socket.send(user['header'] + user['data'] + message_['header'] + message_['data'])
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]













