
import unittest

def square(x):
    return x ** 2

class TestSquare(unittest.TestCase):

    def setUp(self):
        self.x = 5

    def test_square(self):
        self.assertEqual(square(self.x), 25)

    def tearDown(self):
        print("Test completed!")

if __name__ == "__main__":
    unittest.main()
