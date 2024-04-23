
import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert_equal(self):
        self.assertEqual(self.a, 10)

    def test_assert_not_equal(self):
        self.assertNotEqual(self.a, 11)

    def test_assert_greater_than(self):
        self.assertTrue(self.a > 9)

    def test_assert_less_than(self):
        self.assertTrue(self.a < 12)

if __name__ == '__main__':
    unittest.main()
