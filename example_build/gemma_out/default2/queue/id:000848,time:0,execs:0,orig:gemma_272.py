
import unittest

def my_function(x, y):
    return x + y


class TestMyFunction(unittest.TestCase):

    def setUp(self):
        self.x = 10
        self.y = 20

    def test_my_function(self):
        self.assertEqual(my_function(self.x, self.y), 30)


if __name__ == "__main__":
    unittest.main()

