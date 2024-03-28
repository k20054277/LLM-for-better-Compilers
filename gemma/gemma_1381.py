
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        self.my_string = "Hello, world!"

    def test_assert(self):
        self.assertEqual(self.my_string, "Hello, world!")

    def test_issubclass(self):
        self.assertTrue( issubclass(MyTest, unittest.TestCase) )


if __name__ == "__main__":
    unittest.main()
