import socket
import threading
import socketserver
import time
import ServerDo
import include.Decode
import include.Encode
import json
import threading

lock = threading.Lock()
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):#inherit class -  socketserver.BaseRequestHandler

    def handle(self):
        while True:
            data = str(self.request.recv(1024), 'ascii')
            dec = include.Decode.Decode(msg=data, srclen=6, deslen=12)
            print(data)
            dec.set_msg(data)
            dec.decode()
            instruction ={}
            with lock:
                #write data to j_data.json
                j_data = dec.to_json(type='data')
                with open("../json/j_data.json", 'r') as load_f:
                    load_dict = json.load(load_f)

                load_dict[j_data['src_addr']] = j_data
                with open('../json/j_data.json', 'w') as f:
                    json.dump(load_dict, f)
                    print("wrote -> ../include/j_data.json")

                #read instruction from j_instruction.json
                with open("../json/j_instruction.json", 'r') as instruction_f:
                    instruction = json.load(instruction_f)
            str_instruction = json.dumps(instruction)
            if len(instruction) > 0 and dec.src_addr == list(instruction.keys())[0]:
                print("instruction:",instruction, "指令读完了")
                self.request.sendall(str_instruction.encode())
            else:
                print("instruction",instruction,'还没有指令')
                self.request.sendall(bytes(data, 'ascii'))
            # cur_thread = threading.current_thread()
            # print(cur_thread.name)
            time.sleep(1)



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 6999

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    with open('../json/j_data.json', 'w') as f:
        f.write('{}')
    with server:
        ip, port = server.server_address
        print(ip, port)
        # Start a thread with the server -- that thread will then start one
        # more thread for each request
        server_thread = threading.Thread(target=server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()
        print("Server loop running in thread:", server_thread.name)
        while True:
            a = 1
        server.shutdown()