"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is developing the consle-menu for the reception pi.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""

#!/usr/bin/env python3
import sqlite3
from bcrypt import hashpw, gensalt,checkpw
import sys
from validation import validate
from passlib.hash import sha256_crypt

# a local database stroing user's infomation when they register
databaseName='C:/Users/jasco/Desktop/IOT_sphinx_demo/src/profile.db'
conn=sqlite3.connect(databaseName)

class menu():
    """The menu object implements a console-menu based system for reception pi . It displays
    selection for LMS users. New user will sign up with needed information and store in local 
    Sqlite3 dababase. Existing user uses unique email address and password to log in.

    Email address parameter will be set a primary key and pass to the other python file as a variable.

    Notes:
    For running this application ,you need to use  Python 3.*,other version will be not supported.
    Also you need to install necessary libraries for different modules.A simple command line will be:
    pip3 install (module_name)

    Make sure you have your own local Sqlite3 database created before running this application,see more at 'createdb.py' file.
    """
    def display_menu(self):
        #: Display menu when True
        while True:
            #: print a line with 30 "-" + MENU + 30 "-" , start of the menu
            print (30 * "-" , "MENU" , 30 * "-")
            #: print console menu 
            print ("Welcome\n")
            print ("Please select you want to start:")
            print ("1. Sign Up ")
            print ("2. Log in ")
            print ("\n0. Quit")
            print (67 * "-") #: print a line with 67 "-" ,end of the menu

            #: The input field with message prompt on the screen 
            #: the value will be passed by named "choice" to if-else statement
            choice=input("Enter your choice: ")    

            #: Import validation.py script and named: check()
            #: check() contains all functions in validate class
            check=validate()

            #: The if-elif-else statement is geeting choice parameter in the above input function
            #: Compare the value and constant number 1,2,3,4 to go to different situations
            if choice ==("1"):
                username=check.check_username() #: using validate function to create validated varabile
                hashPassword=check.check_password() #: using validate function to create validated varabile
                name=check.check_name() #: using validate function to create validated varabile
                email=check.check_email()   #: using validate function to create validated varabile
                curs=conn.cursor()
                curs.execute("INSERT INTO profile_user VALUES ((?),(?),(?),(?))", (username,hashPassword,name,email))   #: all validated varabiles are incerting to the local database
                conn.commit()
                print("\nSigned up,please log in\n")
                
            elif choice==("2"):
                user_Email,passWord=check.check_login_status() #: using validate function to valid input value
                
            elif choice==("0"):
                
                sys.exit() #: safety exit the application

            else :
                print("Invalid selection,please enter number 1 or 2 or 0") #input error,loop back to selection 
                return

def main():
    a=menu()
    a.display_menu()

main()