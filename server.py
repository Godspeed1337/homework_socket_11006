import socket
from _thread import start_new_thread

host = '192.168.191.182'
port = 5555
thread_count = 0

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(5)
print('Server is running. Press ctrl+c to stop')
print('Listening for connections')


def client_talk_first(connection, neighb_conn):
    connection.send(str.encode('Neighbour founded'))
    while True:
        try:
            data = connection.recv(1024)
        except:
            break
        print(str(data))
        if not data:
            break
        neighb_conn.send(data)
    connection.close()
    neighb_conn.close()


def client_talk_second(connection, neighb_conn):
    connection.send(str.encode('Neighbour founded, pls wait message from neighbour'))
    while True:
        try:
            data = connection.recv(1024)
        except:
            break
        print(str(data))
        if not data:
            break
        neighb_conn.send(data)
    connection.close()
    neighb_conn.close()


while True:
    conn, address = serversocket.accept()
    print(f'New connection established: {address}')
    thread_count += 1
    print(f'Thread number: {thread_count}')
    conn.send(str.encode('Wait a neighbour'))

    conn2, address2 = serversocket.accept()
    print(f'New connection established: {address2}')
    thread_count += 1
    print(f'Thread number: {thread_count}')
    conn2.send(str.encode('Wait a neighbour'))

    start_new_thread(client_talk_first, (conn, conn2))
    start_new_thread(client_talk_second, (conn2, conn))

