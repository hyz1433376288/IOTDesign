import socket
import threading
import socketserver
import time
import ClientDo
import include.Encode
import include.Decode

def client(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((ip, port))
        enc = include.Encode.Encode(temperature_cnt=2
             , humidity_cnt=1
             , airconditioner_cnt=2
             , light_turn_cnt=2
             , light_adjust_cnt=2
             , window_cnt=1)
        mac = "axb56y"
        host = "127000000001"
        message = ClientDo.set_msg(mac=mac, host=host, data=enc.msg)

        while True:
            print("sent message", message)
            sock.sendall(bytes(message, 'ascii'))
            response = str(sock.recv(1024), 'ascii')

            print("Has been set: {}".format(response))
            if "#" not in response:
                ClientDo.set_device(response) # response host-mac-data inner decode the response and set
                                                                                       #data
            nextmsg = ClientDo.update(head_temp_humi=enc.encode(), tail_setted_device= response[len(mac) + len(host):], temp_humi_len=enc.temperature_cnt*3+enc.humidity_cnt*2 + 2)
            nextmsg = ClientDo.set_msg(mac=mac, host=host, data=nextmsg)
            message = nextmsg
            time.sleep(1)

ip, port = "localhost", 6999

client(ip, port)

