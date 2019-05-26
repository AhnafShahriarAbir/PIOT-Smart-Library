#!/usr/bin/env python3
import sqlite3
from bcrypt import hashpw, gensalt,checkpw
import sys
from client import Client
from validation import validate
from passlib.hash import sha256_crypt
from facial_re import recognise

databaseName='profile.db'
conn=sqlite3.connect(databaseName)


class menu():
    def display_menu(self):
        while True:
            print (30 * "-" , "MENU" , 30 * "-")
            print ("Welcome\n")
            print ("Please select you want to start:")
            print ("1. Sign Up ")
            print ("2. Log in with email")
            print ("3. Facial login")
            print ("\n0. Quit")
            print (67 * "-")
            choice=input("Enter your choice: ")    
            check=validate()
            #recogn = recognise() 
            if choice ==("1"):
                username=check.check_username()
                hashPassword=check.check_password()
                name=check.check_name()
                email=check.check_email()
                curs=conn.cursor()
                curs.execute("INSERT INTO profile_user VALUES ((?),(?),(?),(?))", (username,hashPassword,name,email))
                conn.commit()
                print("\nSigned up,please log in\n")

            elif choice == ("2"):
                user_Email, password = check.check_login_status()
                print(user_Email)
                Client.get_details(user_Email)

            elif choice==("3"):            
                #user_Email=recogn.facial_recognise()
                Client.get_details(user_Email)

            elif choice==("0"):
                
                sys.exit()

            else :
                print("Invalid selection,please enter number 1 or 2 or 0")
                return

def main():
    a=menu()
    a.display_menu()

main()