
import unittest

def square(x):
    return x**2

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.x = 5

    def test_square(self):
        self.assertEqual(square(self.x), 25)

    def test_square_rounded(self):
        self.assertEqual(round(square(self.x)), 25)

if __name__ == '__main__':
    unittest.main()
