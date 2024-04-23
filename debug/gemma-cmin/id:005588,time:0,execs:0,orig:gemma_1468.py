
import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert(self):
        self.assertEqual(self.a, 10)

    def test_argument(self, num):
        self.assertEqual(num, 20)


if __name__ == '__main__':
    unittest.main()
