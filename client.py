#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket

HOST = "10.132.109.173"

# HOST = "127.0.0.1" # The server's hostname or IP address.
PORT = 65001         # The port used by the server.
ADDRESS = (HOST, PORT)


class Client():
    """This function is for the reception pi connect to the master pi by using socket programming.
    For sending and receving encoded message,the user_email is passing from local database and displayed to the
    Matser Pi for showing information.  

    """
    def get_details(user_email):
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print("Connecting to Server")
                s.connect(ADDRESS)               
                s.sendall(user_email.encode())  #: sending encoded primary key to master pi
                data=s.recv(4096)
                if (data.decode()=="logout"):   #: If decoded message is equal to "Logout",Mp receive message
                    print("logout")
                    break
                
            
            
        
        
        
