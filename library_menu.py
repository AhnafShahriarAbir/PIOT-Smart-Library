#!/usr/bin/env python3
import sqlite3
import sys

# databaseName = 'dummy_library.db'
# conn = sqlite3.connect(databaseName)


class library_menu():
    def display_menu():
        while True:
            print(30 * "-", "LIBRARY MENU", 30 * "-")
            print("Welcome to the library, " )
            print("Please select you want to start:")
            print("1. Search Book/ Borrow Book")
            print("2. Return ")
            print("3. Logout")
            print(" ")
            print(67 * "-")
            choice = input("Enter your choice: ")

            if choice == ("1"):
                
                print("\n Searching for book \ Borrow Book \n")

            elif choice == ("2"):
                print("Returning book")

            elif choice == ("3"):
                break

            else:
                print("Invalid selection,please enter number 1, 2 or 3")
                return