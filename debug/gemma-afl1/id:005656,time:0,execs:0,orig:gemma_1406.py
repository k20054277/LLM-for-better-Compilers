
import unittest

class MyClass(unittest.TestCase):

    @staticmethod
    def my_static_method():
        return 10

    def test_my_static_method(self):
        self.assertEqual(MyClass.my_static_method(), 10)

if __name__ == "__main__":
    unittest.main()
