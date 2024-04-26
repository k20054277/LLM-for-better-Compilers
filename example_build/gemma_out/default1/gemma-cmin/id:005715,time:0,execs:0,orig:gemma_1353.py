
import unittest

class TestAssertAndBytearray(unittest.TestCase):

    def setUp(self):
        self.byte_array = bytearray(b"Hello, world!")

    def test_assert_equal(self):
        self.assertEqual(self.byte_array, bytearray(b"Hello, world!"))

    def test_assert_in(self):
        self.assertTrue(b"world" in self.byte_array)

    def test_assert_not_in(self):
        self.assertFalse(b"Foo" in self.byte_array)


if __name__ == "__main__":
    unittest.main()
