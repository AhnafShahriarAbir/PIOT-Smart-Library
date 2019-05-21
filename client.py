    
#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket

HOST = "192.168.0.120"

# HOST = "127.0.0.1" # The server's hostname or IP address.
PORT = 65001         # The port used by the server.
ADDRESS = (HOST, PORT)


class Client():
    def get_details(user_email):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print("Connecting to Server")
                s.connect(ADDRESS)
                
                s.sendall(user_email.encode())
                data=s.recv(4096)
                if (data.decode()=="logout"):
                    print("logout")
                    break
                

