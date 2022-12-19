from os import fork
import socket
from _thread import *
from prometheus import PONGS_TOTAL, startMetricHandle

def handle_client(address,conn):
        print("Connection from: " + str(address), flush=True)
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data), flush=True)
            data = "pong"
            conn.send(data.encode())  # send data to the client
            PONGS_TOTAL.labels(address=str(address[0])).inc()

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port not above 1024

    server_socket = socket.socket()  # get socket
    try:
        server_socket.bind((host, port))  # bind host address and port to socket
    except socket.error as e:
        print(str(e))
        return -1
    # configure how many client the server can listen simultaneously
    server_socket.listen(3)
    while True:
        try:
            conn, address = server_socket.accept()  # accept new connection
            start_new_thread(handle_client, (address,conn,)) # handle connection async
        except Exception as e:
            print(str(e))
            break

    server_socket.close() # close the connection
    return -2

if __name__ == '__main__':
    startMetricHandle()
    server_program()