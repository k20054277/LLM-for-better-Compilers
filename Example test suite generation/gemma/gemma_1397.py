
import unittest

class TestClass(unittest.TestCase):

    @property
    def setUp(self):
        self.x = 10

    @assert
    def test_assert(self):
        self.assertEqual(self.x, 10)

    @assert
    def test_assert_equal(self):
        self.assertEqual(self.x, 10)

    @assert
    def test_assert_not_equal(self):
        self.assertNotEqual(self.x, 11)


if __name__ == "__main__":
    unittest.main()
