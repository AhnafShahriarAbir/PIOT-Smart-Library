#!/usr/bin/env python3
import sqlite3
import sys
import socket
from calendarEvent import CalendarEvent
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
            print(70 * "-")
            choice = input("Enter your choice: ")

            create = DatabaseUtils()
            event = CalendarEvent()
            userID = create.getUserID(user_email)
            if choice == ("1"):
                bookName = input("Enter the name of the book: ")
                result = create.searchBook(bookName)
                if not result or len(bookName) == 0:
                    print("Invalid input or Book doesnt exist!")
                    continue
                print('\nSEARCH RESULTS:\n')
                for row in result:
                    print('ID: ', row[0], ' TITLE: ', row[1], ' AUTHOR: ', row[2], 'STATUS: ', row[3])
                userInput = input(
                    "\nEnter ID of the Book to borrow \nPress any other key to return to the menu\n")
                for row in result:
                    if userInput == str(row[0]) and row[3] == 'Available':
                        tableData = create.checkTable(userInput)
                        if not tableData:
                            create.borrowBook(row[0], row[1], userID)
                            eventID = event.addEvent(row[1])
                            create.eventTable(row[0], eventID)
                            print("\nBOOK BORROWED!")
                        else:
                            print("BOOK ALREADY BORROWED!")
                    elif userInput == str(row[0]) and row[3] == 'Unavailable':
                        print("That book is not available.")
                print(70 * "-")
                continue

            elif choice == ("2"):
                print("BOOKS BORROWED:")
                result = create.showBorrowedBooks(userID)

                if not result:
                    print("You have not borrowed any books yet.")
                else:
                    for row in result:
                        print('ID: ', row[0], ' TITLE: ', row[1])
                    userInput = input(
                        "Enter the ID of the book you want to return: ")
                    for row in result:
                        if userInput == str(row[0]):
                            create.returnBook(userInput)
                            eventID = create.getEventID(userInput)
                            for row in eventID:
                                print('ID: ', row[0])
                            print(row[0])
                            event.deleteEvent(row[0])
                            create.deleteEvent(userInput)
                            print("BOOK RETURNED!")
                        else:
                            print(
                                "Enter ID of the Book to borrow \nPress any other key to return to the menu\n")
                print(70 * "-")
                continue

            elif choice == ("3"):
                print("Logging Out")
                print(70 * "-")
                sys.exit()

            else:
                print("Invalid selection,please enter number 1, 2 or 3")
                continue

    display_menu('saif.zeo@gmail.com')
