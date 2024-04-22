
import unittest

def my_function(x):
    return x * x

class TestMyFunction(unittest.TestCase):

    def setUp(self):
        self.x = 5

    def test_my_function(self):
        self.assertEqual(my_function(self.x), 25)

    def tearDown(self):
        print("Test completed!")

if __name__ == "__main__":
    unittest.main()
