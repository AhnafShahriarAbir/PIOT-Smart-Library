#!/usr/bin/env python3
import sqlite3
import sys
import socket
from databaseUtils import DatabaseUtils

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

            create = DatabaseUtils()
            if choice == ("1"):
                title = input("Enter name of the book: ")
                print("Searching book")
                searchResult = create.searchBook(title)
                print(searchResult)
                #borrow = input("Enter ID of the Book you want to borrow: ")

            elif choice == ("2"):
                print("Returning book")
                create.showBorrowedBooks(user_email)
                bookID = input("Enter the ID of the book you want to return: ")
                create.returnBook(bookID)

            elif choice == ("3"):
                print("enter any key to exit.....")
                print("log out")
                sys.exit()

            else:
                print("Invalid selection,please enter number 1, 2, 3 or 4")
                return

    display_menu('saif.zeo@gmail.com')