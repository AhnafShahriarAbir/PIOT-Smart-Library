#!/usr/bin/env python3
import sqlite3
from bcrypt import hashpw, gensalt,checkpw
import sys
import re
databaseName='/home/pi/A2/profile.db'
conn=sqlite3.connect(databaseName)

class validate():
    def check_username(self):
        username=input("Enter your username : ")
        while True:
            if len(username) < 7:
                if re.match("^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]*$", username) != None:
                    print("Valid user name")
                    break
            else :
                print("Invalid user name")
            
        self.username=username
        return (self.username)
    
    def check_password(self):
        while True:
            password=input("Enter your password : ")
            confirmed_password=input("Enter your password again: ")   
            if (len(password)<6 or len(password)>12):
                print("password length is between 6 to 12,please check and enter again")

            elif not re.search("[a-zA-Z]",password):
                print("password needs at least one character,please check and enter again")

            elif not re.search("[0-9]",password):
                print("password needs at least one number,please check and enter again")

            elif not re.search("[$#@]",password):
                print("password needs at least one symbol($#@),please check and enter again")

            elif re.search(r'\s',password):
                print("password can not allow space,please check and enter again")

            elif password != confirmed_password:
                print("Incorrect password mathcing")

            else:
                True
                print("valid password")
                break

        hashPassword=hashpw(password.encode('utf8'), gensalt(13))
        #print(hashPassword)
        self.hashPassword=hashPassword
        self.password=password
        return (self.hashPassword,self.password)

    def check_name(self):
        fname=input("Enter your first name : ")
        lname=input("Enter your last name : ")
        
        while True:
            name=fname+lname
            if name.isalpha():
                full_name=fname+" "+lname
                break
            else:
                print("Please enter characters A-Z only")
        self.name=full_name
       
        return (self.name)

    def check_email(self):
        email=input("Enter your email :")
        while True:

            if re.match("^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]*$", email) is None:
                print("Valid email address")
                break
            elif len(email)< 7:
                print("Invalid email address")              
            else:
                print("Invalid email address")
        self.email=email

        return (self.email)

    def check_login_status(self):
        userName=input("Enter your username : ")
        passWord=input("Enter password : ")
        #hashPassWord=hashpw(passWord.encode('utf8'), gensalt(13))
        #print(hashPassWord)
        #if (checkpw(passWord, hashPassWord)) is not None:
            #print("Correct Password")
        curs=conn.cursor()
        curs.execute('SELECT * FROM profile_user_login WHERE username =(?) AND password=(?)',(userName,passWord,))
        if curs.fetchone() is None:            
            print ("Login failed,try again")
        else:
            print ("Welcome!"+userName)
            
            #break

        self.userName=userName
        self.passWord=passWord
        return(self.userName,self.passWord)
        
