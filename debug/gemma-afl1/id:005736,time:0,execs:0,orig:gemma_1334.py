
import unittest

class TestMyCode(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert_equal(self):
        self.assertEqual(self.a, 10)

    def test_in_operator(self):
        self.assertTrue(self.a in (10, 20, 30))

if __name__ == '__main__':
    unittest.main()
