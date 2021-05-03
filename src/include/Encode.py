import random
class Encode:
    msg = ""
    temperature_cnt = 0
    humidity_cnt = 0

    airconditioner_cnt = 0
    light_turn_cnt = 0
    light_adjust_cnt = 0
    window_cnt = 0
    new_temp_humi = ''
    new_device_state = ''
    def __init__(self, temperature_cnt, humidity_cnt, airconditioner_cnt, light_turn_cnt, light_adjust_cnt, window_cnt):
        # the number of devices below can not be change once current client connect with server
        self.temperature_cnt = temperature_cnt
        self.humidity_cnt = humidity_cnt

        # the values of those device below only generate once (first time)
        self.airconditioner_cnt = airconditioner_cnt
        self.light_turn_cnt = light_turn_cnt
        self.light_adjust_cnt = light_adjust_cnt
        self.window_cnt = window_cnt
        self.new_temp_humi += str(self.temperature_cnt)
        self.new_temp_humi += self.__random_data(cnt=self.temperature_cnt, maxv=100, width=3)
        self.new_temp_humi += str(self.humidity_cnt)
        self.new_temp_humi += self.__random_data(cnt=self.humidity_cnt, maxv=99, width=2)

        self.new_device_state += str(self.airconditioner_cnt)
        for i in range(self.airconditioner_cnt):
            self.new_device_state += self.__random_data(cnt=1, maxv=9,width=1)
            self.new_device_state += self.__random_data(cnt=1, maxv=99,width= 2)
            self.new_device_state += self.__random_data(cnt=1, maxv=9,width=1)
        self.new_device_state += str(self.light_turn_cnt)
        self.new_device_state += self.__random_data(cnt=self.light_turn_cnt, maxv=1, width=1)
        self.new_device_state += str(self.light_adjust_cnt)
        self.new_device_state += self.__random_data(cnt=self.light_adjust_cnt, maxv=100, width=3)
        self.new_device_state += str(self.window_cnt)
        self.new_device_state += self.__random_data(cnt=self.window_cnt, maxv=1,width=1)
        self.msg = self.new_temp_humi + self.new_device_state
        print(self.msg)
    def __random_data(self, cnt, maxv, width):
        res = ""
        for i in range(cnt):
            if width == 1:
                res += "{:0>1d}".format(random.randint(0, maxv))
            elif width == 2:
                res += "{:0>2d}".format(random.randint(0, maxv))
            elif width == 3:
                res += "{:0>3d}".format(random.randint(0, maxv))
        # print(res)
        return res


    def encode(self):
        # update temperature and humidity
        self.new_temp_humi = ""
        self.new_temp_humi += str(self.temperature_cnt)
        self.new_temp_humi += self.__random_data(cnt=self.temperature_cnt, maxv=100, width=3)
        self.new_temp_humi += str(self.humidity_cnt)
        self.new_temp_humi += self.__random_data(cnt=self.humidity_cnt, maxv=99, width=2)
        # only override temp and humidity while remain device state
        self.msg = self.new_temp_humi + self.new_device_state
        print(self.msg)
        return self.msg
    def set_device(self, json_instruction):
        res = ''
        mac = list(json_instruction.keys())[0]
        print(mac,"Encode.py def set_device()")
        for kk in ['airconditioner', 'light_turn', 'light_adjust', 'window']:#had better avoid use the key in dict ,keep device identical  order with the previous
            if kk == 'airconditioner':
                res += str(len(json_instruction[mac][kk]))
                for ac in json_instruction[mac][kk]:
                    for kkk in ac:
                        if kkk == 'mode' or kkk == 'wind':
                            res += "{:0>1d}".format(ac[kkk])
                        elif kkk == 'temperature':
                            # print("ackk",ac[kk])
                            # print("temp:::","{:0>2d}".format(ac[kkk]))
                            res += "{:0>2d}".format(ac[kkk])
            elif kk == 'light_adjust':
                res += str(len(json_instruction[mac][kk]))
                for v in json_instruction[mac][kk]:
                    res += "{:0>3d}".format(v)
            elif kk == 'window' or 'light_turn':
                res += str(len(json_instruction[mac][kk]))
                for v in json_instruction[mac][kk]:
                    res += "{:0>1d}".format(v)
        self.new_device_state = res
        print("new_device_state：",self.new_device_state)
