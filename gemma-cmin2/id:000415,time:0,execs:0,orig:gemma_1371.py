
import unittest

class MyClass(unittest.TestCase):

    def setUp(self):
        self.my_obj = MyObject()

    def test_getattr(self):
        self.assertEqual(getattr(self.my_obj, 'name'), 'John Doe')

    def test_assert(self):
        assert self.my_obj.name == 'John Doe'

# Create an instance of the test class and run the tests
if __name__ == '__main__':
    unittest.main()
