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
            print("1. Search Book Catalogue and Borrow ")
            print("2. Return ")
            print("3. Logout")
            print(" ")
            print(67 * "-")
            choice = input("Enter your choice: ")

            create = DatabaseUtils()
            userID = create.getUserID(user_email)
            if choice == ("1"):
                bookName = input("Enter name of the book: ")
                print("Searching book")
                bookID, title = create.searchBook(bookName)
                print('\nSEARCH RESULTS:\n')
                print('ID: ', bookID, ' TITLE: ', title)
                inp = input("\nEnter ID of the Book to borrow \nPress any other key to return to the menu\n")
                if inp == str(bookID):
                    create.borrowBook(bookID, title, userID)
                    print("\nBOOK BORROWED!")
                else:
                    return        

            elif choice == ("2"):
                print("Returning book")
                bookID, title = create.showBorrowedBooks(userID)
                print('ID: ', bookID, ' TITLE: ', title)
                inp = input("Enter the ID of the book you want to return: ")
                create.returnBook(inp)
                print("BOOK RETURNED!")

            elif choice == ("3"):
                print("Logging Out")
                sys.exit()

            else:
                print("Invalid selection,please enter number 1, 2, 3 or 4")
                return

    display_menu('saif.zeo@gmail.com')