#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
from library_menu import library_menu
HOST = "172.20.10.3"

# HOST = "127.0.0.1" # The server's hostname or IP address.
PORT = 65001         # The port used by the server.
ADDRESS = (HOST, PORT)


class Client():
    def get_details(user_email):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting to Server")
            s.connect(ADDRESS)

            s.sendall(user_email.encode())
            data = s.recv(4096)
            library_menu.display_menu(user_email)
        print("Done.")
        
        
