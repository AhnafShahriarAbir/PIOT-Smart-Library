import unittest
import pymysql
import json
from adminUtils import DatabaseUtils


class TestDatabaseUtils(unittest.TestCase):

    with open("cloudConnection.json") as read:
        data = json.load(read)
    HOST = data['host']
    USER = data['user']
    PASSWORD = data['password']
    DATABASE = data['database']

    def setUp(self):
        self.connection = pymysql.connect(TestDatabaseUtils.HOST, TestDatabaseUtils.USER,
            TestDatabaseUtils.PASSWORD, TestDatabaseUtils.DATABASE)

    def tearDown(self):
        try:
            self.connection.close()
        except:
            pass
        finally:
            self.connection = None

    def countBook(self):
        with self.connection.cursor() as cursor:
            cursor.execute("select count(*) from Book")
            return cursor.fetchone()[0]
    
    def test_insertBook(self):
        with DatabaseUtils(self.connection) as db:
            count = self.countBook()
            self.assertFalse(db.insertBook("Pokemon", "Jack"))
            self.assertTrue(count + 1 == self.countBook())
            self.assertFalse(db.insertBook("Digimon", "Jones"))
            self.assertTrue(count + 2 == self.countBook())

    def test_showBook(self):
        with DatabaseUtils(self.connection) as db:
            self.assertTrue(self.countBook() == len(db.showBooks()))

if __name__ == "__main__":
    unittest.main()
