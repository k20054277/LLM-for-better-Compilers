
import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        self.my_obj = MyClass()

    def test_has_attr(self):
        self.assertTrue( hasattr(self.my_obj, 'my_attr'))

    def test_assert_equal(self):
        self.assertEqual(self.my_obj.my_attr, 10)


if __name__ == '__main__':
    unittest.main()
