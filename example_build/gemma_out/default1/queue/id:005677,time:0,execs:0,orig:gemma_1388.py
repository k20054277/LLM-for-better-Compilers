
import unittest

class TestAssertAndMemoryview(unittest.TestCase):

    def setUp(self):
        self.arr = memoryview(int, 10)

    def test_assert_equal(self):
        self.assert_equal(self.arr[0:5], [0, 1, 2, 3, 4])

    def test_assert_not_equal(self):
        self.assert_not_equal(self.arr[0:5], [0, 2, 3, 4, 5])

    def test_memoryview_buffer(self):
        self.assertEqual(self.arr.buffer_info(), (10, 4, 0))

if __name__ == "__main__":
    unittest.main()
