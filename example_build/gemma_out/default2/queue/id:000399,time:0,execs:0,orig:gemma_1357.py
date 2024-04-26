
import unittest

class MyClass(unittest.TestCase):

    def setUp(self):
        self.my_obj = MyClass()

    def test_my_method(self):
        self.assertEqual(self.my_obj.my_method(), 10)

    @classmethod
    def setUpClass(cls):
        print("Setting up class")

    @classmethod
    def tearDownClass(cls):
        print("Tearing down class")


if __name__ == "__main__":
    unittest.main()
