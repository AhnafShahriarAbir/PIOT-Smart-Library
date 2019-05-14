#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket
from library_menu import library_menu
HOST = ""

PORT = 65001
ADDRESS = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDRESS)
    s.listen()
    
    print("Listening on {}...".format(ADDRESS))
    conn, addr = s.accept()
    with conn:

        while True:
            data = conn.recv(4096)
            if(not data):
                break
            
            user = data.decode()
            print("User connected: " + user)
            library_menu.display_menu(user)
	    
            logout_message = " logged out"
            conn.sendall(logout_message.encode())
            data = conn.recv(4096)
        
        print("Disconnecting from client.")
    print("Closing listening socket.")
print("Done.")
