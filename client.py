    
#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket

HOST = "10.132.130.121"

# HOST = "127.0.0.1" # The server's hostname or IP address.
PORT = 65001         # The port used by the server.
ADDRESS = (HOST, PORT)


class Client():
    def get_details(user_email):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(ADDRESS)

            print("Connecting to Server")
            s.connect(ADDRESS)
            data = s.recv(4096)

            s.sendall(user_email.encode())
            s.listen()
            data = s.recv(4096)
            user = data.decode()
            print("User logged out: " + user)
            
        print("Done.")
        