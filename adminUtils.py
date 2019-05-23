import pymysql
import json


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

    def insertBook(self, title, author):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Book (Title, Author) values (%s, %s)", (title, author))
        self.connection.commit()

    def deleteBook(self, BookID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM Book WHERE BookID = %s", (BookID))
        self.connection.commit()
    
    def showBooks(self):
        result = ''
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID, Title, Author FROM Book")
            result = cursor.fetchall()
            return result