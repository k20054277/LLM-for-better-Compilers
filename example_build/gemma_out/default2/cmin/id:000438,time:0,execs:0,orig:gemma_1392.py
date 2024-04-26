
import unittest

class TestOctal(unittest.TestCase):

    def test_octal_conversion(self):
        self.assertEqual(oct(10), 8)

    def test_assert_greater_than(self):
        self.assertGreater(10, 5)

if __name__ == "__main__":
    unittest.main()
