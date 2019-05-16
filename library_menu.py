#!/usr/bin/env python3
import sqlite3
import sys
import socket
#from add_event import CreateEvent
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
            #event = CreateEvent()
            userID = create.getUserID(user_email)
            if choice == ("1"):
                bookName = input("Enter name of the book: ")
                print('\nSEARCH RESULTS:\n')
                result = create.searchBook(bookName)
                for row in result:
                    print('ID: ', row[0], ' TITLE: ', row[1])
                userInput = input("\nEnter ID of the Book to borrow \nPress any other key to return to the menu\n")

                create.borrowBook(bookID, title, userID)
                #event.addEvent(title)
                print("\nBOOK BORROWED!")

            elif choice == ("2"):
                print("Returning book")
                result = create.showBorrowedBooks(userID)

                if not result:
                    print("You have not borrowed any books yet.")
                else:
                    for row in result:
                        print('ID: ', row[0], ' TITLE: ', row[1])

                    userInput = input("Enter the ID of the book you want to return: ")
                    create.returnBook(userInput)
                    print("BOOK RETURNED!")
                return

            elif choice == ("3"):
                print("Logging Out")
                sys.exit()

            else:
                print("Invalid selection,please enter number 1, 2, 3 or 4")
                return

    display_menu('saif.zeo@gmail.com')
