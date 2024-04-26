
import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert(self):
        self.assertEqual(self.a, 10)

    def test_double(self):
        self.assertTrue(self.a * 2 > 10)

if __name__ == '__main__':
    unittest.main()
