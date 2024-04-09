
import unittest

def filter_even(nums):
    return [num for num in nums if num % 2 == 0]

class TestFilterEven(unittest.TestCase):

    def setUp(self):
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_filter_even(self):
        self.assertEqual(filter_even(self.nums), [2, 4, 6, 8, 10])

if __name__ == '__main__':
    unittest.main()
