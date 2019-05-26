import unittest
import pymysql
import json
from databaseUtils import DatabaseUtils


class TestDatabaseUtils(unittest.TestCase):

    with open("cloudConnection.json") as read:
        data = json.load(read)
    HOST = data['host']
    USER = data['user']
    PASSWORD = data['password']
    DATABASE = data['database']

    def tearDown(self):
        try:
            self.connection.close()
        except:
            pass
        finally:
            self.connection = None

    def setUp(self):
        self.connection = pymysql.connect(TestDatabaseUtils.HOST, TestDatabaseUtils.USER,
                                          TestDatabaseUtils.PASSWORD, TestDatabaseUtils.DATABASE)

    def countEvent(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Events")
            return cursor.fetchone()[0]

    def countBook(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from BookBorrowed")
            return cursor.fetchone()[0]

    def bookExists(self, bookID):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "select count(*) from BookBorrowed where bookID = %s", (bookID,))
            return cursor.fetchone()[0] == 1

    def bookSearch(self, bookName):
        with self.connection.cursor() as cursor:
            cursor.execute(
                "select count(*) from Book where bookID = %s", (bookName,))
            return cursor.fetchone()[0]

    def test_eventTable(self):
        with DatabaseUtils(self.connection) as db:
            count = self.countEvent()
            self.assertFalse(db.eventTable("10", "abcdefgh"))
            self.assertTrue(count + 1 == self.countEvent())
            self.assertFalse(db.eventTable("11", "zxcvbnm"))
            self.assertTrue(count + 2 == self.countEvent())

    def test_borrowBook(self):
        with DatabaseUtils(self.connection) as db:
            count = self.countBook()
            self.assertFalse(db.borrowBook("1", "Cat", "1"))
            self.assertTrue(count + 1 == self.countBook())
            self.assertFalse(db.borrowBook("2", "Dog", "1"))
            self.assertTrue(count + 2 == self.countBook())

    def test_returnBook(self):
        with DatabaseUtils(self.connection) as db:
            count = self.countBook()
            bookID = 1
            self.assertTrue(self.bookExists(bookID))
            db.returnBook(bookID)
            self.assertFalse(self.bookExists(bookID))
            self.assertTrue(count - 1 == self.countBook())

    def test_searchBook(self):
        with DatabaseUtils(self.connection) as db:
            count = self.bookSearch("the")
            self.assertFalse(count == len(db.searchBook("the")))


if __name__ == "__main__":
    unittest.main()
