#!/usr/bin/env python3
import sqlite3
from bcrypt import hashpw, gensalt,checkpw
import sys
from validation import validate

databaseName='/home/pi/A2/profile.db'
conn=sqlite3.connect(databaseName)

class menu():
    def display_menu(self):
        while True:
            print (30 * "-" , "MENU" , 30 * "-")
            print ("Welcome\n")
            print ("Please select you want to start:")
            print ("1. Sign Up ")
            print ("2. Log in ")
            print ("\n0. Quit")
            print (67 * "-")
            choice=input("Enter your choice: ")    
            check=validate()
            if choice ==("1"):
                username=check.check_username()
                hashPassword,password=check.check_password()
                name=check.check_name()
                email=check.check_email()
                curs=conn.cursor()
                curs.execute("INSERT INTO profile_user VALUES ((?),(?),(?),(?))", (username,hashPassword,name,email))
                curs.execute("INSERT INTO profile_user_login VALUES ((?),(?))", (username,password))
                conn.commit()
                print("\nSigned up,please log in\n")
                
            elif choice==("2"):
                userName,passWord=check.check_login_status()
                #userName=input("Enter your username : ")
                #passWord=input("Enter your password : ")
                hashPassWord=hashpw(passWord.encode('utf8'), gensalt(13))
                #checkpw(passWord, hashPassWord):
                #curs=conn.cursor()
                #curs.execute('SELECT * FROM profile_user WHERE username =(?) AND password=(?)',(userName,hashPassWord,)) 
                #if curs.fetchone() is not None:
                    #print ("Welcome")
                #else:
                    #print ("Login failed")

            elif choice==("0"):
                sys.exit()

            else :
                print("Invalid selection,please enter number 1 or 2 or 0")
                return

def main():
    a=menu()
    a.display_menu()

main()