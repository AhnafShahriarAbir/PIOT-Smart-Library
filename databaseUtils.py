import pymysql


class DatabaseUtils():
    HOST = "35.244.94.254"
    USER = "root"
    PASSWORD = "password"
    DATABASE = "lms"

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

    def createBookTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Book(
                    BookID int not null auto_increment,
                    Name text not null,
                    constraint FK_BookID foreign key (BookID)
                )""")
        self.connection.commit()

    def createBorrowedBookTable(self):
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists  BorrowedBook (
                    BorrowedBook int not null auto_increment,
                    Name text not null,
                    constraint FK_BorrowedBook foreign key (BorrowedBook)
                )""")
        self.connection.commit()

    def createUserTable(self):
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
        with self.connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists Event (
                    EventID int not null auto_increment,
                    Name text not null,
                    constraint PK_EventID primary key (EventID)
                )""")
        self.connection.commit()

    def insertBook(self, title, author):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Book (Title, Author) values ((?), (?))", (title, author))
        self.connection.commit()

        return cursor.rowcount == 1

    def addUser(self, username, name, email):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO LmsUser (UserName, Name, Email) values (%s, %s, %s)", (username, name, email))
        self.connection.commit()

    def checkTable(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID FROM BookBorrowed WHERE BookID = %s", (bookID))
            result = cursor.fetchall()
            return result

    def deleteBook(self, BookID):
        with self.connection.cursor() as cursor:
            cursor.execute("delete from Person where BookID = %s", (BookID))
        self.connection.commit()

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
            rows = cursor.fetchall()
            return rows
    
    def searchBookByID(self, id):
        """
            This method searches the database with given bookid as 
            the parameter. 
            Then calls the return book method and passes the id as
            parameter to return the book.
            author: @shahriar_abir
        """
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE BookId = %s", (id))
            row = cursor.fetchone()
            print(row)
            self.returnBook(id)
        self.connection.commit()

    def showBorrowedBooks(self, userID):
        result = ''
        with self.connection.cursor() as cursor:
            cursor.execute(
                "SELECT BookID, Title FROM BookBorrowed WHERE LmsUserID = %s", (userID))
            result = cursor.fetchall()
            return result

    def returnBook(self, bookID):
        """
            This method takes bookID as a parameter. 
                Deletes the row from BookBorrrowed table where BookId is the parameter
                Updates status of the book to 'Available'
                Deletes the event that was created when borrowing the book. 
            author: @shahriar_abir
        """
        with self.connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM BookBorrowed WHERE BookID = %s", (bookID))
            cursor.execute(
                "UPDATE Book SET Status = 'Available' WHERE BookID = %s", (bookID))
            self.deleteEvent(bookID)
        self.connection.commit()

    def borrowBook(self, bookID, title, userID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO BookBorrowed (BookID, Title, LmsUserID) VALUES (%s, %s, %s)", (bookID, title, userID))
            cursor.execute(
                "UPDATE Book SET Status = 'Unavailable' WHERE BookID = %s", (bookID))
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
