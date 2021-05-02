# import socket
# import time
# def client(ip, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#
#         sock.connect((ip, port))
#         message = "123"
#         while True:
#             print("sent message", message)
#             sock.sendall(bytes(message, 'ascii'))
#             time.sleep(1)
#
#
# client(ip='localhost', port=5000)
#
#

import requests
url = "http://localhost:3000//"
data = {"key":"value"}
res = requests.post(url=url,data=data)
print(res.text)