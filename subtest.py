import socket
import threading
import socketserver
import time

def client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        for i in range(0,5):
            sock.connect((ip, port))
            # while True:

            sock.sendall(bytes(message, 'ascii'))
            sock.sendall(bytes(message, 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            print("Received: {}".format(response))
            time.sleep(1)

ip, port = "localhost", 6999

client(ip, port, "Hello World 1")

