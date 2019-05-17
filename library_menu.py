#!/usr/bin/env python3
import sqlite3
import sys
import socket
from calendarEvent import CreateEvent
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
            event = CreateEvent()
            userID = create.getUserID(user_email)
            if choice == ("1"):
                bookName = input("Enter the name of the book: ")
                result = create.searchBook(bookName)
                if not result or len(bookName) == 0:
                    print("Invalid input or Book doesnt exist!")
                    return
                print('\nSEARCH RESULTS:\n')
                for row in result:
                    print('ID: ', row[0], ' TITLE: ', row[1])
                userInput = input(
                    "\nEnter ID of the Book to borrow \nPress any other key to return to the menu\n")
                for row in result:
                    if userInput == str(row[0]):
                        tableData = create.checkTable(userInput)
                        if not tableData:
                            create.borrowBook(row[0], row[1], userID)
                            print("\nBOOK BORROWED!")
                            event.addEvent(row[1])
                        else:
                            print("BOOK ALREADY BORROWED!")
                print(67 * "-")
                continue
                
            elif choice == ("2"):
                print("Returning book")
                result = create.showBorrowedBooks(userID)

                if not result:
                    print("You have not borrowed any books yet.")
                else:
                    for row in result:
                        print('ID: ', row[0], ' TITLE: ', row[1])

                    userInput = input(
                        "Enter the ID of the book you want to return: ")
                    create.returnBook(userInput)
                    print("BOOK RETURNED!")
                print(67 * "-")
                continue

            elif choice == ("3"):
                print("Logging Out")
                print(67 * "-")
                sys.exit()

            else:
                print("Invalid selection,please enter number 1, 2, 3 or 4")
                continue

    display_menu('saif.zeo@gmail.com')
