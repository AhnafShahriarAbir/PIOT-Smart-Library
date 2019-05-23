"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is developing the consle-menu for the Master pi after successfully log in.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""
#!/usr/bin/env python3
import sqlite3
import sys
import socket
from calendarEvent import CalendarEvent
from databaseUtils import DatabaseUtils
from barcode_scanner import barcode
from searchByBookName import VoiceSearch
create = DatabaseUtils()
event = CalendarEvent()

class library_menu():
    """This library_menu class is another console-based applicaiton supporting the menu.py. After successed log in attempt,
    Menu.py will direct and turn to execute this script.

    The library_menu class displays the next console menu for LMS users once they log in to the application. 
    """
    def display_menu(self, user_email):
        """Passing the primary key from last console based menu and start to display another console based menu. Providing users selection
        to make next command.
        
        The display_menu(user_eamil) function implements a certain amount of code for add/delete/update a database with few different
        table by calling google cloud platform, all the data store in the google cloud , calling method via MySQL query.

        By printing out selected data to the consloe menu, user input their selection accordinlgy.
        
        """
        while True:
            print(30 * "-", "LIBRARY MENU", 30 * "-")   #: print a line with 30 "-" + MENU + 30 "-",start of the menu 
            print("Welcome to the library, " + user_email)
            print("Please select you want to start:")
            print("1. Search Book Catalogue and Borrow ")
            print("2. Return ")
            print("3. Logout")
            print(" ")
            print(70 * "-") #: print a line with 67 "-" ,end of the menu
            
            #: The input field with message prompt on the screen 
            #: the value will be passed by named "choice" to if-else statement
            choice = input("Enter your choice: ")

            userID = create.getUserID(user_email)   #:assign the userID by passing the value from calendarEvent
            if choice == ("1"): # :print the selection for master pi
                print("Choose an option to Search for Book:")
                print("1. Search by Book name")
                print("2. Use voice search")
                option = input("Enter the selection: ")

                if option == ("1"):
                    self.getBookByName(userID)
    
                elif option == ("2"):   #:boost up the voice search function
                    vc = VoiceSearch()  #:voice to text
                    result = vc.main()
                    if result is None:
                        self.getBookByName(userID)
                print(70 * "-")
                continue
                
            elif choice == ("2"):
                print("BOOKS BORROWED:")
                result = create.showBorrowedBooks(userID)   # select filted data from the database 
                if not result:
                    print("You have not borrowed any books yet.")   #: message for no result founding 
                    return

                else:
                    for row in result:
                        print('ID: ', row[0], ' TITLE: ', row[1])   #: print out all the borrowed book
                print("")
                print("Choose an option to return:")
                print("1. Return by ID:")
                print("2. Return by scanning QR code ")
                option = input("Enter the selection: ")

                if option == ("1"):
                    userInput = input(
                        "Enter the ID of the book you want to return: ")
                    for row in result:
                        if userInput == str(row[0]):    #: match the book id with user input
                            create.returnBook(userInput)    #: delete and update the specific row with the bookID in database
                            eventID = create.getEventID(userInput)  #: add event to the calendar according to the bookID and status
                            for row in eventID:
                                event.deleteEvent(row[0])
                            create.deleteEvent(userInput)
                            print("BOOK RETURNED!")
                        else:
                            print(
                             "Enter ID of the Book to borrow \nPress any other key to return to the menu\n")
                elif option == ("2"):
                    barCode = barcode() # boost up the barcode scan function, if barcode scann and decode as bookID,execute next command
                    barCode.getQR()
                    print("Book returned.")
                    
                print(70 * "-")
                continue

            elif choice == ("3"):    #:log out from the master pi
                print("Logging Out...")
                print(70 * "-")
                return  # :loop back to the listening 

            else:
                print("Invalid selection,please enter number 1, 2 or 3")
                continue

    def getBookByName(self, userID):
        bookName = input("Enter the name of the book: ")
        result = create.searchBook(bookName)
        if not result or len(bookName) == 0:
            print("Invalid input or Book doesnt exist!")    #：error message for getting book name 
            
        print('\nSEARCH RESULTS:\n')
        for row in result:
            print('ID: ', row[0], ' TITLE: ', row[1],
                    '   AUTHOR: ', row[2], 'STATUS: ', row[3])  #: print all the result in the table

        userInput = input(
            "\nEnter ID of the Book to borrow \nPress any other key to return to the menu\n")
        for row in result:
            if userInput == str(row[0]) and row[3] == 'Available':  #: the book status shows available,and execute the if statement
                tableData = create.checkTable(userInput)
                if not tableData:   #: if no event found ,create new event
                    create.borrowBook(row[0], row[1], userID)   #: add to the borrow book table for new borrow
                    eventID = event.addEvent(row[1])    #: add new event to the event table 
                    create.eventTable(row[0], eventID)
                    print("\nBOOK BORROWED!")
                else:
                    print("BOOK ALREADY BORROWED!")
            elif userInput == str(row[0]) and row[3] == 'Unavailable':  #: check status
                print("That book is not available.")
