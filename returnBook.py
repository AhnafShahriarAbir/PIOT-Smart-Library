def returnBook(self, name):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM BorrowedBook WHERE (Name) values (%s)", (name))
        self.connection.commit()

def borrowBook(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO BorrowedBook (LmsUserID) SELECT (LmsUserID) FROM LmsUser")
            cursor.execute("INSERT INTO BorrowedBook (BookID, Title) SELECT (BookID, Title) FROM Book WHERE (BookID) values (%s)", (bookID))
        self.connection.commit()