
import unittest

class TestMyClass(unittest.TestCase):

    def setUp(self):
        self.my_obj = MyClass()

    def test_my_method(self):
        self.assertEqual(self.my_obj.my_method(), 10)

    def tearDown(self):
        print("Test completed!")


class MyClass:

    def my_method(self):
        return 10


if __name__ == "__main__":
    unittest.main()
