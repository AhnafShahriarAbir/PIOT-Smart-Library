#!/usr/bin/env python3
import sqlite3
from passlib.hash import sha256_crypt
import sys
import re

databaseName = 'profile.db'
conn = sqlite3.connect(databaseName)


class validate():
    # The check_username() requirement user enter their user name,
    # length should be less than 7,valid input is number,character ,"_""-"
    def check_username(self):
        while True:
            username = input("Enter your username : ")
            if len(username) < 10:
                if re.match("^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]*$", username) is not None:
                    print("Valid user name")
                    break

            else:
                False
                print("Invalid user name")
        self.username = username
        return (self.username)
    # The check_password() will ask user
    # enter password for twice,the password will be :

    # length between 6 to 12
    # at least one character
    # at least one number
    # at least one symbol between "[!@#$]"
    # space is not allowed

    def check_password(self):
        while True:
            password = input("Enter your password : ")
            confirmed_password = input("Enter your password again: ")

            if (len(password) < 6 or len(password) > 12):
                print("""password length is between 6 to 12,
                please check and enter again""")

            elif not re.search("[a-zA-Z]", password):
                print("""password needs at least one character,
                    please check and enter again""")

            elif not re.search("[0-9]", password):
                print("""password needs at least one number,
                    please check and enter again""")

            elif not re.search("[!$#@]", password):
                print("""password needs at least one symbol(!$#@),
                    please check and enter again""")

            elif re.search(r'\s', password):
                print("""password can not allow space,
                please check and enter again""")

            elif password != confirmed_password:
                print("Incorrect password mathcing")

            else:
                print("valid password")
                break
        hashedPassword = sha256_crypt.hash(password)

        self.hashedPassword = hashedPassword

        return (self.hashedPassword)

    # The check_name() will ask user to enter first name and last name,
    # then check if it is alphabetically
    def check_name(self):
        while True:
            fname = input("Enter your first name : ")
            lname = input("Enter your last name : ")
            name = fname+lname
            if name.isalpha():
                full_name = fname+" "+lname
                break
            else:
                print("Please enter characters A-Z only")
                break
        self.name = full_name
        return (self.name)

    # The check_email() will ask user enter email address and check the style
    def check_email(self):
        while True:
            email = input("Enter your email :")
            curs=conn.cursor()
            curs.execute('SELECT * FROM profile_user WHERE Email =(?)',(email,))
            result = curs.fetchone()
            if (result is not None):
                False
                print("Email is already used,please use another one.")
                # TO DO ----------------- check for existing email in database ------------
            elif (re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)):
                print("Valid email address")
                # conn.close()
                break
            else:
                False
                print("Invalid email,try again")

        self.email = email

        return (self.email)

    # The check_login_tatus() will ask user to enter their
    # signed email address and password,
    def check_login_status(self):
        while True:
            user_email = input("Enter your email address : ")
            passWord = input("Enter password : ")
            curs = conn.cursor()
            curs.execute('SELECT * FROM profile_user WHERE Email =(?)',(user_email,))
            results = curs.fetchone()
            print(results)
            if results is None:
                print("User is not found!")
            else:
                    if sha256_crypt.verify(passWord, results[1]):
                        print("Login successful for  "+results[0])
                        break
                    else:
                        print ("Incorrect password,please check!")
                
            

        self.user_email=user_email
        self.passWord=passWord
        return(self.user_email,self.passWord)
        
