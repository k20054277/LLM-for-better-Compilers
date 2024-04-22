
import unittest

class TestAssertAndSlash(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 3

    def test_assert_equal(self):
        self.assertEqual(self.a + self.b, 13)

    def test_slash_operator(self):
        self.assertEqual(self.a // self.b, 3)

if __name__ == "__main__":
    unittest.main()
