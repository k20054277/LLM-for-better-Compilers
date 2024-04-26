
import unittest

def my_function(x):
    return x + 1

class TestMyFunction(unittest.TestCase):

    def setUp(self):
        self.x = 10

    def test_my_function(self):
        self.assertEqual(my_function(self.x), 11)

    def tearDown(self):
        print("Test complete!")

if __name__ == "__main__":
    unittest.main()
