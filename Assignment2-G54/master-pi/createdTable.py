"""
    PIOT SMART LIBRARY 
    ~~~~~~~~~
    This part is developing the console-menu for the Master pi after successfully log in and redirect.
    :copyright: © 2019 by the PIOT group 54 team.
    :license: BSD, see LICENSE for more details.
"""

import pymysql
import json

class DatabaseUtils():
    """"This class has all the function supporting the library_menu.py , by connecting to the google cloud and required different action.
    
    """
    with open("cloudConnection.json") as read:
        data = json.load(read)
    HOST = data['host']
    USER = data['user']
    PASSWORD = data['password']
    DATABASE = data['database']

    def __init__(self, connection=None):
        """ connect to the database
        """
        if(connection == None):
            connection = pymysql.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
                                         DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
        self.connection = connection

    def close(self):
        #: colse the connection
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def createBookTable(self):
        """create the BookTable table with defined parameter and figure
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Book(
                    BookID int not null auto_increment,
                    Name text not null,
                    constraint FK_BookID foreign key (BookID)
                )""")
        self.connection.commit()

    def createBorrowedBookTable(self):
        """create the BorrowedBookTable table with defined parameter and figure
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists  BorrowedBook (
                    BorrowedBook int not null auto_increment,
                    Name text not null,
                    constraint FK_BorrowedBook foreign key (BorrowedBook)
                )""")
        self.connection.commit()

    def createUserTable(self):
        """create the UserTable table with defined parameter and figure
        """
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists LmsUser (
                    LmsUserID int not null auto_increment,
                    Name text not null,
                    constraint FK_UserID foreign key (UserID)
                    constraint UN_UserName unique (UserName)
                )""")
        self.connection.commit()

    def createEventTable(self):
        """create the EventTable table with defined parameter and figure
        """       
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Event (
                    EventID int not null auto_increment,
                    Name text not null,
                    constraint PK_EventID primary key (EventID)
                )""")
        self.connection.commit()

    def insertBook(self, title, author):
        """add value to the table 
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Book (Title, Author) values ((?), (?))", (title, author))
        self.connection.commit()

        return cursor.rowcount == 1

    def addUser(self, username, name, email):
        """add row to the table 
        """        
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO LmsUser (UserName, Name, Email) values (%s, %s, %s)", (username, name, email))
        self.connection.commit()

    def checkTable(self, bookID):
        """filter and check row from the table 
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID FROM BookBorrowed WHERE BookID = %s", (bookID))
            result = cursor.fetchall()
            return result

    def deleteBook(self, BookID):
        """delete row to the table 
        """
        with self.connection.cursor() as cursor:
            cursor.execute("delete from Person where BookID = %s", (BookID))
        self.connection.commit()

    def getUserID(self, email):
        """find and match value in a row from the table 
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT LmsUserID FROM LmsUser WHERE Email = %s", (email))
            result = cursor.fetchall()
            return result

    def searchBook(self, bookName):
        """get value in a row and fetch with all satisfied rows
        """
        result = ""
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM Book WHERE Title LIKE %s", ("%" + bookName + "%"))
            result = cursor.fetchall()
            return result

    def showBorrowedBooks(self, userID):
        """get value in a row and fetch with all satisfied rows
        """
        result = ''
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID, Title FROM BookBorrowed WHERE LmsUserID = %s", (userID))
            result = cursor.fetchall()
            return result

    def returnBook(self, bookID):
        """get value in a row and delet with the specific rows in BookBorrowed table
        Update the row['Status'] accordingly 
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM BookBorrowed WHERE BookID = %s", (bookID))
            cursor.execute(
                "UPDATE Book SET Status = 'Available' WHERE BookID = %s", (bookID))
        self.connection.commit()

    def borrowBook(self, bookID, title, userID):
        """add row to table 
        Update the row['Status'] accordingly 
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO BookBorrowed (BookID, Title, LmsUserID) VALUES (%s, %s, %s)", (bookID, title, userID))
            cursor.execute(
                "UPDATE Book SET Status = 'Unavailable' WHERE BookID = %s", (bookID))
        self.connection.commit()

    def eventTable(self, bookID, eventID):
        """Add row to the event table accordin to the bookID adn eventID
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Events (BookID, ID) VALUES (%s, %s)", (bookID, eventID))
        self.connection.commit()

    def deleteEvent(self, bookID):
        """get value in a row and delete with the specific rows in Events table
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Events WHERE BookID = %s", (bookID))
        self.connection.commit()

    def getEventID(self, bookID):
        """get value in a row and fetch with the specific rows in Events table
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT ID FROM Events WHERE BookID = %s", (bookID))
            result = cursor.fetchall()
            return result

if __name__ == "__main__":
   DatabaseUtils()