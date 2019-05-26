"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is developing the console-menu for admin on the Master pi.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""

import pymysql
import json


class DatabaseUtils():
    """This class is developing a flask-based HTML for admin user only. It is associating with the template and bootstrap .
    This is a separate website application that runs on MP. It can only be accessed by admin personnal.The admin can access the add book,
    delete book and view daily,weeekly date report by quering and filtering data from google cloud database.

    With the adding book, admin insert book to the database table

    With the delete book, admin delete the book from the database table

    With the data report, admin select the date or a period (week) to view the book borrowed adn retun stauts in a graph.

    """
    #: admin credential is loaded from JSON file

    # host – Host where the database server is located
    # user – Username to log in as
    # password – Password to use.
    # database – Database to use, None to not use a particular one.
    with open("cloudConnection.json") as read:
        data = json.load(read)
    HOST = data['host']
    USER = data['user']
    PASSWORD = data['password']
    DATABASE = data['database']

    #: connecting to the google cloud database
    def __init__(self, connection=None):
        if(connection == None):
            connection = pymysql.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
                                         DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
        self.connection = connection

    # Send the quit message and close the socket.
    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    #: admin add books to the book table with book name and author
    def insertBook(self, title, author):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Book (Title, Author) values (%s, %s)", (title, author))
        self.connection.commit()  # :Commit changes to stable storage.
        
        return cursor.rowcount == 1

    #: admin delete books from the book table with bookID
    def deleteBook(self, BookID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Book WHERE BookID = %s", (BookID))
        self.connection.commit()  # :Commit changes to stable storage.

    #: fetch books from the book table with book details
    def showBooks(self):
        result = ''
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID, Title, Author FROM Book")
            result = cursor.fetchall()
            return result
