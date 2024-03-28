
import unittest

class TestPow(unittest.TestCase):

    def setUp(self):
        self.x = 2
        self.y = 3

    def test_pow(self):
        self.assertEqual(pow(self.x, self.y), 8)

    def test_assert(self):
        assert pow(self.x, self.y) == 8


if __name__ == "__main__":
    unittest.main()
