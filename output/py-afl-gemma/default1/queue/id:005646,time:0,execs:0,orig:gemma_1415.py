
import sys
import unittest

def division(a, b):
    return a / b

class TestDivision(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 2

    def test_division(self):
        self.assertEqual(division(self.a, self.b), 5)

    def tearDown(self):
        print("Test completed!")

if __name__ == "__main__":
    unittest.main()
