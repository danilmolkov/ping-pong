import socket
import time
import random
from datetime import datetime
from prometheus import PINGS_TOTAL, startMetricHandle

def client_program() -> int:
    host = "server"  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    try:
        client_socket.connect((host, port))  # connect to the server
    except socket.error as e:
        print(str(e))
        return -1
    message = "ping"
    random.seed(datetime.now().timestamp())
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Received from server: ' + data, flush=True)  # show in terminal
        PINGS_TOTAL.inc()
        time.sleep(random.randint(5,15))

    client_socket.close()  # close the connection
    return -2

if __name__ == '__main__':
    startMetricHandle()
    client_program()