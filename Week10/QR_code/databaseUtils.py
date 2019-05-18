import pymysql


class DatabaseUtils():
    HOST = "35.244.94.254"
    USER = "root"
    PASSWORD = "password"
    DATABASE = "lms"

    def __init__(self, connection = None):
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
            cursor.execute("INSERT INTO Book (Title, Author) values ((?), (?))", (title, author))
        self.connection.commit()

        return cursor.rowcount == 1

    def getBook(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select BookID, Title, Author from Book")
            result = cursor.fetchall()
            for row in result:
                print('ID:', row[0], 'TITLE:', row[1], 'AUTHOR:', row[2])

    def deleteBook(self, BookID):
        with self.connection.cursor() as cursor:
            cursor.execute("delete from Person where BookID = %s", (BookID))
        self.connection.commit()
        
    def searchBook(self, title):
        bookID = ""
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM Book WHERE Title = %s", (title))
            result = cursor.fetchall()
            for row in result:
                bookID = row[0]
                print("Book Title: " + row[1] + " Author: " + row[2])
            return bookID
        self.connection.commit()

    def searchBookByID(self, id):
        with self.connection.cursor() as cursor:
            row = cursor.execute("SELECT * FROM Book WHERE BookId = %s", (id))
            print(row)
            returnBook(id)
        self.connection.commit()

    def showBorrowedBooks(self, email):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM BookBorrowed WHERE LmsUserID = LmsUserID FROM LmsUser WHERE Email = %s", (email))
            result = cursor.fetchall()
            for row in result:
                print('ID:', row[0], 'Title:', row[1])
        self.connection.commit()

    def returnBook(self, ID):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE * FROM BookBorrowed WHERE BookBorrowedID = %s", (ID))
        self.connection.commit()
        
    def borrowBook(self, bookID, email):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO BookBorrowed (BookID, Title) SELECT BookID, Title FROM Book WHERE BookID = %s AND INSERT INTO BookBorrowed Email values (%s)", (bookID, email))
        self.connection.commit()
