
import unittest

class TestAssertAndLoop(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3, 4, 5]

    def test_assert_and_loop(self):
        for num in self.data:
            self.assertEqual(num, num**2)

if __name__ == '__main__':
    unittest.main()
