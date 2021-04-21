class decode:

    msg = "" #recieved string from client
    src_addr = "" #client head
    SRC_ADDR_LEN = 6
    des_addr = ""
    DES_ADDR_LEN = 12

    temperature_cnt = 0
    temperature = []
    humidity_cnt = 0
    humidity = []
    class airCdt:
        def __init__(self, ac_mode, ac_temperature, ac_wind):
            self.ac_mode = ac_mode
            self.ac_temperature = ac_temperature
            self.ac_wind = ac_wind
        def __str__(self):
            return "mode:{} temperature:{} wind:{}".format(self.ac_mode, self.ac_temperature, self.ac_wind)

    airconditioner_cnt = 0
    airconditioner = [] #element type is object airCdt
    light_turn_cnt = 0
    light_turn = []
    light_adjust_cnt = 0
    light_adjust = []
    window_cnt = 0
    window = []

    msg_ptr = 0
    def __init__(self, msg, srclen, deslen):
        self.msg = msg
        self.SRC_ADDR_LEN = srclen
        self.DES_ADDR_LEN = deslen

    def scan_address(self):
        # can not invoke scan_forward() ,because addr is not integer
        self.src_addr = self.msg[self.msg_ptr:self.SRC_ADDR_LEN]
        self.msg_ptr += self.SRC_ADDR_LEN
        self.des_addr = self.msg[self.msg_ptr:self.msg_ptr + self.DES_ADDR_LEN]
        self.msg_ptr += self.DES_ADDR_LEN

    def scan_forward(self, length):
        # print(self.msg)
        end = self.msg_ptr + length
        if end > len(self.msg):
            print("out of the length of msg")
            return 0
        res = int(self.msg[self.msg_ptr:end])
        self.msg_ptr += length
        print(res)
        return res

    def scan_temperature(self):
        self.temperature_cnt = self.scan_forward(1)
        for i in range(0, self.temperature_cnt):
            print("temperature")
            self.temperature.append(self.scan_forward(3))

    def scan_humidity(self):
        self.humidity_cnt = self.scan_forward(1)
        for i in range(0, self.humidity_cnt):
            print("humidity")
            self.humidity.append(self.scan_forward(2))

    def scan_airconditioner(self):
        self.airconditioner_cnt = self.scan_forward(1)
        for i in range(0, self.airconditioner_cnt):
            print("airconditioner")
            mode = self.scan_forward(1)
            temperature = self.scan_forward(2)
            wind = self.scan_forward(1)
            self.airconditioner.append(self.airCdt(mode, temperature, wind))
            print(self.airconditioner[-1])

    def scan_light_turn(self):
        print("light_turn")
        self.light_turn_cnt = self.scan_forward(1)
        for i in range(0, self.light_turn_cnt):
            self.light_turn.append(self.scan_forward(1))

    def scan_light_adjust(self):
        print("light_adjust")
        self.light_adjust_cnt = self.scan_forward(1)
        for i in range(0, self.light_adjust_cnt):
            self.light_adjust.append(self.scan_forward(3))

    def scan_window(self):
        print("window")
        self.window_cnt = self.scan_forward(1)
        for i in range(0, self.window_cnt):
            self.window.append(self.scan_forward(1))
    def decode(self):
        self.scan_address()
        self.scan_temperature()
        self.scan_humidity()
        self.scan_airconditioner()
        self.scan_light_turn()
        self.scan_light_adjust()
        self.scan_window()

s = decode("abcdef127000000001202205629989283697378211209909811",6,12)
print("mac = ",s.src_addr)
print("des = ",s.des_addr)
s.decode()





