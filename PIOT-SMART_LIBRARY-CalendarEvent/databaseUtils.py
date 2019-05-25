import pymysql
import json
import datetime


class DatabaseUtils():

    with open("cloudConnection.json") as read:
        data = json.load(read)
    HOST = data['host']
    USER = data['user']
    PASSWORD = data['password']
    DATABASE = data['database']

    def __init__(self, connection=None):
        if(connection == None):
            connection = pymysql.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
                                         DatabaseUtils.PASSWORD, DatabaseUtils.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def checkTable(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID FROM BookBorrowed WHERE BookID = %s", (bookID))
            result = cursor.fetchall()
            return result

    def getUserID(self, email):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT LmsUserID FROM LmsUser WHERE Email = %s", (email))
            result = cursor.fetchall()
            return result

    def searchBook(self, bookName):
        result = ""
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM Book WHERE Title LIKE %s", ("%" + bookName + "%"))
            result = cursor.fetchall()
            return result

    def showBorrowedBooks(self, userID):
        result = ''
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID, Title FROM BookBorrowed WHERE LmsUserID = %s", (userID))
            result = cursor.fetchall()
            return result

    def returnBook(self, bookID):
        returnDate = datetime.date.today()
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM BookBorrowed WHERE BookID = %s", (bookID))
            cursor.execute(
                "UPDATE Book SET Status = 'Available' WHERE BookID = %s", (bookID))
            cursor.execute(
                "UPDATE Graph SET Returned = Returned + 1 WHERE Time = %s", (returnDate,))
        self.connection.commit()

    def borrowBook(self, bookID, title, userID):
        borrowDate = datetime.datetime.now()
        print(borrowDate)
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO BookBorrowed (BookID, Title, LmsUserID) VALUES (%s, %s, %s)", (bookID, title, userID))
            cursor.execute(
                "UPDATE Book SET Status = 'Unavailable' WHERE BookID = %s", (bookID))
            cursor.execute(
                "UPDATE Graph SET Borrowed = Borrowed + 1 WHERE Time = %s", (borrowDate,))
        self.connection.commit()

    def eventTable(self, bookID, eventID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Events (BookID, ID) VALUES (%s, %s)", (bookID, eventID))
        self.connection.commit()

    def deleteEvent(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Events WHERE BookID = %s", (bookID))
        self.connection.commit()

    def getEventID(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT ID FROM Events WHERE BookID = %s", (bookID))
            result = cursor.fetchall()
            return result
