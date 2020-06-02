
import socket
import time
# localIP = "10.52.3.25"
localIP = "127.0.0.1"
# localIP = '25.135.227.60'
localPort   = 20001
bufferSize  = 1000

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening...")


def sendToClients(typeOfMessage, address, message, clients):
    name = ''
   #getting the name of the sender 
    for c in clients: 
        if c[1] == address[1]:
            name = clients[address]


    # Sending a reply to client
    for c in clients:
        if c[1] != address[1]:
            if typeOfMessage == '$msg#':
                header = f'$msg#{len(name + b">>" + message)}'.encode('utf-8')
                UDPServerSocket.sendto(header, c)
                UDPServerSocket.sendto(name + b'>>' + message, c)
            elif typeOfMessage == '$ou#+':
                UDPServerSocket.sendto(message, c)
            elif typeOfMessage == '$file$l#':
                header = f'$file$l#{len(message[0])}'.encode('utf-8')
                UDPServerSocket.sendto(header, c)
                UDPServerSocket.sendto(message[0], c)
                UDPServerSocket.sendto(message[1], c)
            elif typeOfMessage == 'notify':
                UDPServerSocket.sendto(message.encode('utf-8'), c)
            elif typeOfMessage == 'fileData':
                UDPServerSocket.sendto('$fileData$'.encode('utf-8'), c)
                #skipping the first packet
                for seq, pk in message[1:]:
                    UDPServerSocket.sendto(seq, c)
                    time.sleep(.5)
                    UDPServerSocket.sendto(pk, c)

#list of clients 
clients = {}
# Listen for incoming datagrams
while(True):
    message_header =  UDPServerSocket.recvfrom(10)
    address = message_header[1]
    if '$file$l#' in message_header[0].decode('utf-8'):
        fileLength = message_header[0].decode('utf-8').strip().split('#')[1]
        filename = UDPServerSocket.recvfrom(int(fileLength))[0]
        clean = UDPServerSocket.recvfrom(10)[0]
        f_c = (filename, clean)
        sendToClients('$file$l#', address, f_c, clients)
    elif '$name$#:' in message_header[0].decode('utf-8'):
        name_length = int(message_header[0].decode('utf-8').split(':')[1])
        name = UDPServerSocket.recvfrom(name_length)
        exists = False
        for c in clients: 
            if c[1] == address:
                exists = True
        if not exists:
            clients[address] = name[0]
            continue # do not send names to clients
    elif '$msg#' in message_header[0].decode('utf-8'):
        msgLength = int(message_header[0].decode('utf-8').split('#')[1])
        message = UDPServerSocket.recvfrom(msgLength)
        sendToClients('$msg#', address, message[0], clients)
    elif '$ou#+' in message_header[0].decode('utf-8'):
        sendToClients('$ou#+', address, message_header[0], clients)
    elif '$cancelDd$' in message_header[0].decode('utf-8'):
        sendToClients('notify', address, '$cancelDd$', clients)
    elif '$acceptDd$' in message_header[0].decode('utf-8'):
        sendToClients('notify', address, '$acceptDd$', clients)
    elif 'filep:' in message_header[0].decode('utf-8'):
        packets = []
        seq_num = UDPServerSocket.recvfrom(1000)
        data = UDPServerSocket.recvfrom(1000)
        while True:
            if data[0] == b'':
                break
            packets.append((seq_num[0], data[0]))
            seq_num = UDPServerSocket.recvfrom(50)
            data = UDPServerSocket.recvfrom(1000)
        
        # to test if the order is changed 
        x = list(reversed(packets))
        x.append((seq_num[0], '$#end^$'.encode('utf-8')))

        packets.append((seq_num[0], '$#end^$'.encode('utf-8')))
        sendToClients('fileData', address, x, clients)

