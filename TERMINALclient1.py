import socket
import select
import errno  #to match error codes
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 5000

my_username = input("Type in your username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect((IP, PORT)) #this socket is just connecting to the socket we already binded as the server.

client_socket.setblocking(False)
#With this, the receive functionality won't block the whole app.

encoded_username = my_username.encode('utf-8') #encoding

username_header = f"{len(encoded_username):< {HEADER_LENGTH}}".encode('utf-8')
# print(username_header)

client_socket.send(username_header + encoded_username)


while True:
    
    message = input(f"{my_username}>> ")
    if message:
        message = message.encode('utf-8')
        message_header = f"{len(message) :< {HEADER_LENGTH}}".encode('utf-8')
        print('#####')
        print(message_header)
        print(message)
        print('#####')
        client_socket.send(message_header + message)
    try: 
        while True:
        #receive things:
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()
            print(username_header)
            username_length = int(username_header.decode('utf-8').strip())
            username = client_socket.recv(username_length).decode('utf-8')
            print("username: ", username)

            message_header = client_socket.recv(HEADER_LENGTH)
            print("Header:", message_header)
            message_length = int(message_header.decode('utf-8').strip())
            print("Length: ", message_length)
            message = client_socket.recv(message_length).decode('utf-8')
            print("message:", message)

            print(f"{username}> {message}")
    
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: ', str(e))
            sys.exit()
        continue
    except Exception as e:
        print('General Error: ', str(e))
        sys.exit()