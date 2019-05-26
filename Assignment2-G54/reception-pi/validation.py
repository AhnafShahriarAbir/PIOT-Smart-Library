#!/usr/bin/env python3
"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part develops and implements a robust input validation scheme.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""
import sqlite3
from passlib.hash import sha256_crypt
import sys
import re

#: provide the directory for local database
databaseName = '/home/pi/A2/profile.db'
# :make connection for the database and pi
conn = sqlite3.connect(databaseName)


class validate():
    """The validate class will get the user input and verify by if-elif-else statement in a while loop.
    This class gurantees the password in a certain high level of secured form.

    """
    # The check_username() requirement user enter their user name,length should be less than 7,valid input is number,character ,"_""-"

    def check_username(self):
        """The check_username() requirement user enter their user name with following standard,
        - length should be less than 7
        - number is allowed,
        - character is allowed 
        - special character "_" and "-" and space is allowed
        """
        while True:
            username = input("Enter your username : ")
            if len(username) < 7:
                if re.match("^[a-zA-Z0-9]+([a-zA-Z0-9](_|-| )[a-zA-Z0-9])*[a-zA-Z0-9]*$", username) != None:
                    print("Valid user name")
                    break
            else:
                False   #: loop back till matched the pattern
                print("Invalid user name")

        self.username = username
        return (self.username)

    def check_password(self):
        """The check_password() will ask user enter password for twice,the password will be :
        - length between 6 to 12 
        - at least one character 
        - at least one number 
        - at least one symbol between "[@#$]" 
        - space is not allowed
        """
        while True:
            password = input("Enter your password : ")
            # : ask user to type password again
            confirmed_password = input("Enter your password again: ")

            if (len(password) < 6 or len(password) > 12):
                print("password length is between 6 to 12,please check and enter again")

            elif not re.search("[a-zA-Z]", password):
                print(
                    "password needs at least one character,please check and enter again")

            elif not re.search("[0-9]", password):
                print("password needs at least one number,please check and enter again")

            elif not re.search("[$#@]", password):
                print(
                    "password needs at least one symbol($#@),please check and enter again")

            elif re.search(r'\s', password):
                print("password can not allow space,please check and enter again")

            elif password != confirmed_password:
                print("Incorrect password mathcing")

            else:
                print("valid password")
                break
        #: The sha256_Crypt.hash() function will take the value from user input and using SHA256 as the algorithm.
        #: SHA256 is inherently better than md5, but you're free to replace "md5" with "sha256" in our above examples to see the hash that is output still remains the same, just a bit longer.
        hashedPassword = sha256_crypt.hash(password)

        self.hashedPassword = hashedPassword

        return (self.hashedPassword)

    def check_name(self):
        """The check_name() will ask user to enter first name and last name, then check if it is alphabetically or not   
        """
        while True:
            fname = input("Enter your first name : ")
            lname = input("Enter your last name : ")
            name = fname+lname
            if name.isalpha():
                full_name = fname+" "+lname
                break
            else:
                print("Please enter characters A-Z only")
        self.name = full_name

        return (self.name)

    def check_email(self):
        """ The check_email() will ask user enter email address and check the style, 
        Specially email as a primary key ,it should be unique and unrepeatable in the database.

        To check if it is unique, open local database and select everything in the table with the user input.
        If find identical value,then it means the email is already signed up before and loop back.
        If there is returning None,which proves the local database has no incerted yet,the email is valided to sign up.
        If email is already existing in the local database,user must choose a new email to terminate the while loop.

        For email,the standard form will be :"something@something.something"
        """
        while True:
            email = input("Enter your email :")
            # :connect to the local database where list above.
            curs = conn.cursor()
            curs.execute(
                'SELECT * FROM profile_user WHERE Email =(?)', (email,))
            result = curs.fetchone()  # : fetch in one means only find one result
            if (result is not None):
                False
                print("Email is already used,please use another one.")
            elif (re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)):
                print("Valid email address")
                # conn.close()
                break   #: if make the required pattern and not repeated in the database,terminate the while loop
            else:
                False
                print("Invalid email,try again")

        self.email = email

        return (self.email)

    def check_login_status(self):
        """The check_login_tatus() will ask user to enter their signed email address and password. Pass the emaill parameter in local database
        to do verification. If email is existed ,go to next verification.

        The sha256_crypt.verify(passWord,results[1]) validate that the two separate hashes came from the source.If the boolean rings True, then match.
        It is because the table profile_user has row for email and hashed password , and email will be unique in the table,so if email is found and we fetch that specific row,
        the hashed password will be taken out and verified. If the user input password is hashed with the same function,then the two source should be matched.
        Once the boolean return true, it means log in success.
        """
        while True:
            user_email = input("Enter your email address : ")
            passWord = input("Enter password : ")
            curs = conn.cursor()
            curs.execute(
                'SELECT * FROM profile_user WHERE Email =(?)', (user_email,))
            results = curs.fetchone()
            if results is None:
                print("User is not found!")
            else:
                if sha256_crypt.verify(passWord, results[1]):
                    # : table profile_user colunm[0] is username.
                    print("Welcome!"+results[0])
                    break
                else:
                    print("Incorrect password,please check!")

        self.user_email = user_email
        self.passWord = passWord
        return(self.user_email, self.passWord)
