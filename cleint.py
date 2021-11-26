import socket




host = '192.168.191.182'
port = 5555

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientsocket.connect((host, port))
except socket.error as e:
    print(e)

response = clientsocket.recv(1024)
print(response.decode())
response = clientsocket.recv(1024)
while not ('Neighbour founded' in response.decode()):
    response = clientsocket.recv(1024)
print(response.decode('utf-8'))
if 'pls wait message from neighbour' in response.decode():
    response = clientsocket.recv(1024)
    print(response.decode('utf-8'))

while True:
    message = input('Enter message: ')
    if not message:
        break
    clientsocket.send(str.encode(message))
    response = clientsocket.recv(1024)
    print(response.decode('utf-8'))
clientsocket.close()
