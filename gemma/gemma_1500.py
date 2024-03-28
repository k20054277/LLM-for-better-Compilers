
import unittest

def my_function(x):
    return x * 2

class TestMyFunction(unittest.TestCase):

    def setUp(self):
        self.x = 5

    def test_my_function(self):
        self.assertEqual(my_function(self.x), 10)

if __name__ == '__main__':
    unittest.main()
