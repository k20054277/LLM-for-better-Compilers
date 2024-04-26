
import unittest

class TestDemo(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert(self):
        self.assertGreater(self.a, 5)

    def test_all(self):
        self.assertTrue(self.a > 5)
        self.assertEqual(self.a, 10)

if __name__ == '__main__':
    unittest.main()
