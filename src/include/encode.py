import random
class encode:
    msg = ""
    temperature_cnt = 0
    humidity_cnt = 0
    class airCdt:
        def __init__(self, ac_mode, ac_temperature, ac_wind):
            self.ac_mode = ac_mode
            self.ac_temperature = ac_temperature
            self.ac_wind = ac_wind

        def __str__(self):
            return "mode:{} temperature:{} wind:{}".format(self.ac_mode, self.ac_temperature, self.ac_wind)

    airconditioner_cnt = 0
    light_turn_cnt = 0
    light_adjust_cnt = 0
    window_cnt = 0
    def __init__(self, temperature_cnt, humidity_cnt, airconditioner_cnt, light_turn_cnt, light_adjust_cnt, window_cnt):
        # the number of devices below can not be change once current client connect with server
        self.temperature_cnt = temperature_cnt
        self.humidity_cnt = humidity_cnt

        # the values of those device below only generate once (first time)
        self.airconditioner_cnt = airconditioner_cnt
        self.light_turn_cnt = light_turn_cnt
        self.light_adjust_cnt = light_adjust_cnt
        self.window_cnt = window_cnt
        self.msg += str(self.temperature_cnt)
        self.msg += self.__random_data(cnt=self.temperature_cnt, maxv=100, width=3)
        self.msg += str(self.humidity_cnt)
        self.msg += self.__random_data(cnt=self.humidity_cnt, maxv=99, width=2)
        self.msg += str(self.airconditioner_cnt)
        for i in range(self.airconditioner_cnt):
            self.msg += self.__random_data(cnt=1, maxv=9,width=1)
            self.msg += self.__random_data(cnt=1, maxv=99,width= 2)
            self.msg += self.__random_data(cnt=1, maxv=9,width=1)
        self.msg += str(self.light_turn_cnt)
        self.msg += self.__random_data(cnt=self.light_turn_cnt, maxv=1, width=1)
        self.msg += str(self.light_adjust_cnt)
        self.msg += self.__random_data(cnt=self.light_adjust_cnt, maxv=100, width=3)
        self.msg += str(self.window_cnt)
        self.msg += self.__random_data(cnt=self.window_cnt, maxv=1,width=1)
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
        new_temp_humi = ""
        new_temp_humi += str(self.temperature_cnt)
        new_temp_humi += self.__random_data(cnt=self.temperature_cnt, maxv=100, width=3)
        new_temp_humi += str(self.humidity_cnt)
        new_temp_humi += self.__random_data(cnt=self.humidity_cnt, maxv=99, width=2)
        # override temp and humi
        self.msg = self.msg[self.temperature_cnt * 3 + self.humidity_cnt * 2 + 2:]
        self.msg = new_temp_humi + self.msg
        print(self.msg)




d = encode(temperature_cnt=2
                    ,humidity_cnt=1
                    ,airconditioner_cnt=2
                    ,light_turn_cnt=2
                    ,light_adjust_cnt=2
                    ,window_cnt=1)
d.encode()
