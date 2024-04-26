
import unittest

def my_function(x):
    if x > 5:
        return True
    else:
        return False

class TestMyFunction(unittest.TestCase):

    def setUp(self):
        self.x = 3

    def tearDown(self):
        self.x = None

    def test_my_function_true(self):
        self.assertEqual(my_function(self.x), True)

    def test_my_function_false(self):
        self.assertEqual(my_function(self.x), False)

if __name__ == "__main__":
    unittest.main()
