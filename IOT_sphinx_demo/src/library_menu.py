"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is developing the consle-menu for the reception pi after successfully log in.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""

#!/usr/bin/env python3
import sqlite3
import sys
import socket
databaseName = 'profile.db'
conn = sqlite3.connect(databaseName)
HOST = "192.168.0.8" # Make sure to update 
# HOST = "127.0.0.1" # The server's hostname or IP address.
PORT = 65001         # The port used by the server.
ADDRESS = (HOST, PORT)

class library_menu():
    """This library_menu class is another console-based applicaiton supporting the menu.py. After successed log in attempt,
    Menu.py will direct and turn to execute this script.

    The library_menu class displays the next console menu for LMS users once they log in to the application. 
    """
    def display_menu(user_email):
        """Passing the primary key from last console based menu and start to display another console based menu. Providing users selection
        to make next command.
        
        """
        while True:
            print(30 * "-", "LIBRARY MENU", 30 * "-")   #: print a line with 30 "-" + MENU + 30 "-",start of the menu 
            print("Welcome to the library, " + user_email)
            print("Please select you want to start:")
            print("1. Search Book catalogue ")
            print("2. Borrow ")
            print("3. Return ")
            print("4. Logout")
            print(" ")
            print(67 * "-") #: print a line with 67 "-" ,end of the menu 

            #: The input field with message prompt on the screen 
            #: the value will be passed by named "choice" to if-else statement
            choice = input("Enter your choice: ")

            if choice == ("1"):
                
                print("\n Searching for book \n")

            elif choice == ("2"):
                print("Borrow book")

            elif choice == ("3"):
                print("Returning book")

            elif choice == ("4"):
                print("enter any key to exit.....")
                print("log out")
                sys.exit()

            else:
                print("Invalid selection,please enter number 1, 2, 3 or 4")
                return
