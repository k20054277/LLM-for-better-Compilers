
import unittest

def is_even(number):
    return number % 2 == 0

class TestEvenNumber(unittest.TestCase):

    def setUp(self):
        self.number = 6

    def test_is_even(self):
        self.assertEqual(is_even(self.number), True)

    def tearDown(self):
        self.number = None

unittest.main()
