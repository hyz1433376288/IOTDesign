import socket
import threading
import socketserver
import time
import ClientDo
import include.Encode
import include.Decode

def client(ip, port, mac):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.connect((ip, port))
        enc = include.Encode.Encode(temperature_cnt=2
             , humidity_cnt=1
             , airconditioner_cnt=2
             , light_turn_cnt=2
             , light_adjust_cnt=2
             , window_cnt=1)
        mac = mac
        host = "127000000001"
        message = ClientDo.set_msg(mac=mac, host=host, data=enc.msg)

        while True:
            print("sent message", message)
            sock.sendall(bytes(message, 'ascii'))
            response = str(sock.recv(1024), 'ascii')
            header = response[:len(mac)+len(host)]
            response = response[len(mac)+len(host):]
            print("Has been set: {}".format(response))
            # if "#" not in response:
            #     ClientDo.set_device(response) # response host-mac-data inner decode the response and set
                                        #old temp_humi_device                           #data
            mid = enc.temperature_cnt*3 + enc.humidity_cnt * 2 + 2
            nextmsg = enc.encode()[0:mid] + response[mid:]
            nextmsg = ClientDo.set_msg(mac=mac, host=host, data=nextmsg)
            message = nextmsg
            time.sleep(1)


client(ip="localhost", port=6999, mac = "pi901m")

