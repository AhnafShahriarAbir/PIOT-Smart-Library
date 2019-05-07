#!/usr/bin/env python3
import sqlite3
import sys
import socket
databaseName = 'profile.db'
conn = sqlite3.connect(databaseName)
HOST = "192.168.0.9"
# HOST = "127.0.0.1" # The server's hostname or IP address.
PORT = 65001         # The port used by the server.
ADDRESS = (HOST, PORT)

class library_menu():
    def display_menu(user_email):
        while True:
            print(30 * "-", "LIBRARY MENU", 30 * "-")
            print("Welcome to the library, " + user_email)
            print("Please select you want to start:")
            print("1. Search Book catalogue ")
            print("2. Borrow ")
            print("3. Return ")
            print("4. Logout")
            print(" ")
            print(67 * "-")
            choice = input("Enter your choice: ")

            if choice == ("1"):
                
                print("\n Searching for book \n")

            elif choice == ("2"):
                print("Borrow book")

            elif choice == ("3"):
                print("Returning book")

            elif choice == ("4"):
                print("enter any key to exit.....")
                sys.exit()

            else:
                print("Invalid selection,please enter number 1, 2, 3 or 4")
                return
