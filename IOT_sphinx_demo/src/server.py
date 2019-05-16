"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is setteing configuration for Master pi
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""
#!/usr/bin/env python3
# Reference: https://realpython.com/python-sockets/
# Documentation: https://docs.python.org/3/library/socket.html

import socket # for socket 
"""HOST = "" # Empty string means to listen on all IP's on the machine, also works with IPv6.
             # Note "0.0.0.0" also works but only with IPv4.
    PORT = 65000 # Port to listen on (non-privileged ports are > 1023).
    # default port for socket

    ADDRESS(HOST,PORT)
    In this example, we’re using socket.AF_INET (IPv4). So it expects a 2-tuple: (HOST,PORT).
    host can be a hostname, IP address, or empty string. If an IP address is used, host should be an IPv4-formatted address string.
    The IP address 127.0.0.1 is the standard IPv4 address for the loopback interface, so only processes on the host will be able to connect to the server. 
    If you pass an empty string, the server will accept connections on all available IPv4 interfaces.
    port should be an integer from 1-65535 (0 is reserved). It’s the TCP port number to accept connections on from clients. 
    Some systems may require superuser privileges if the port is < 1024.
"""

HOST = ""

PORT = 65001
ADDRESS = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDRESS) #: The values passed to bind() depend on the address family of the socket. 
    s.listen()  #: Listen to incoming requests on that ip and port.
                #: A server has a listen() method which puts the server into listen mode. 
                #: This allows the server to listen to incoming connections.
    
    print("Listening on {}...".format(ADDRESS))
    conn, addr = s.accept() #: A server has an accept().The accept method initiates a connection with the client.
                            
    with conn:
    #  After getting the client socket object conn from accept(), an infinite while loop is used to loop over blocking calls to conn.recv(). 
    #: This reads whatever data the client sends and echoes it back using conn.sendall().
    #: If conn.recv() returns an empty bytes object, b'', then the client closed the connection and the loop is terminated. 
    #: The with statement is used with conn to automatically close the socket at the end of the block.

        while True:
            data = conn.recv(4096)
            if(not data):
                break #: disconnect wit the server and terminate the while loop.
                
            print("User connected: " + data.decode()) #: Getting decoded data and print out message to Server
            
            conn.sendall(data)
        print("Disconnecting from client.")
    print("Closing listening socket.")
print("Done.")
