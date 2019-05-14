import MySQLdb

class DatabaseUtils:
    HOST = "35.201.18.142"
    USER = "root"
    PASSWORD = "abc123"
    DATABASE = "Book"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(DatabaseUtils.HOST, DatabaseUtils.USER,
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
                create table if not exists User (
                    UserID int not null auto_increment,
                    Name text not null,
                    constraint FK_UserID foreign key (UserID)
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

    def insertBook(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into Book (BookID, Title, ) values ('%d',' ')", (name,))
        self.connection.commit()

        return cursor.rowcount == 1

    def borrowBook(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute("insert into BorrowedBook (LmsUserID) SELECT (LmsUserID) FROM LmsUser")
            cursor.execute("insert into BorrowedBook (BookID, Title) SELECT (BookID, Title) FROM Book WHERE (BookID) values (%s)", (bookID))
        self.connection.commit()

   

    def returnBook(self, name): 
        with self.connection.cursor() as cursor:
            cursor.execute("delete from BorrowedBook WHERE (title) values (%s)", (name))
        self.connection.commit()

