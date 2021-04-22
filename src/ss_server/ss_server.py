import socket
import threading
import socketserver
import time
import ServerDo
import include.Decode
import include.Encode

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):#inherit class -  socketserver.BaseRequestHandler

    def handle(self):
        while True:
            data = str(self.request.recv(1024), 'ascii')
            print(data)
            cur_thread = threading.current_thread()
            print(cur_thread.name)
            response = ""
            if ServerDo.listen_web():
                pass
            else:
                response = "#"
            self.request.sendall(bytes(response, 'ascii'))
            time.sleep(1)



class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 6999

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
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