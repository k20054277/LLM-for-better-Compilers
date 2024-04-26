
import unittest

class TestFloat(unittest.TestCase):

    def setUp(self):
        self.number = 3.14159

    def test_assert_equal(self):
        self.assertAlmostEqual(self.number, 3.14159)

    def test_assert_greater_than(self):
        self.assertGreater(self.number, 3.1)

    def test_assert_less_than(self):
        self.assertLess(self.number, 3.2)


if __name__ == "__main__":
    unittest.main()
