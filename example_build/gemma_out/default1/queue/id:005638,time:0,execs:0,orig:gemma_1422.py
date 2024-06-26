
import sqlite3
import unittest

# Define a class for testing
class TestSQLite(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('test.db')
        self.c = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_insert(self):
        self.c.execute("""INSERT INTO employees (name, email) VALUES ("John Doe", "john.doe@example.com")""")
        self.c.execute("""SELECT name FROM employees WHERE email = "john.doe@example.com""")
        self.assertEqual(self.c.fetchone()[0], "John Doe")

    def test_select(self):
        self.c.execute("""SELECT * FROM employees""")
        self.assertTrue(len(self.c.fetchall()) > 0)

# Run the tests
if __name__ == '__main__':
    unittest.main()
