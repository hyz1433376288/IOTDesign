import include.Decode
import include.Encode
import os
import shutil

def set_msg(mac, host, data):

    return mac + host + data

def set_device(msg):
    dec = include.Decode.Decode(msg=msg, srclen=12, deslen=6)
    dec.decode()

def update(head_temp_humi, tail_setted_device, temp_humi_len):
    # print("@{}\n@{}".format(head_temp_humi[:temp_humi_len],tail_setted_device[temp_humi_len:]))
    return  head_temp_humi[:temp_humi_len] + tail_setted_device[temp_humi_len:]
# print(update("2046051179282426554210202506200","2013087166292426554210202506211",10))
def makefile(addr, temperature, humidity, data):
    