import unittest
import socket
from client import Client


class testMenu(unittest.TestCase):
    def testServer(self):
        HOST = "10.132.136.121"  # updat the client host as per need
        PORT = 65001         # The port used by the server.
        ADDRESS = (HOST, PORT)
        useremail = "111@gmail.com"
        while True:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                print("Connecting to Server")
                s.connect(ADDRESS)
                # : sending encoded primary key to master pi
                s.sendall(useremail.encode())
                data = s.recv(4096)
                self.assertEqual(data.decode(), "111@gmail.com")
                break


if __name__ == "__main__":
    unittest.main()
