
import unittest

class TestDemo(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert_equal(self):
        self.assertEqual(self.a, 10)

    def test_assert_not_equal(self):
        self.assertNotEqual(self.a, 20)

    def test_assert_greater_than(self):
        self.assertGreater(self.a, 5)

    def test_assert_less_than(self):
        self.assertLess(self.a, 15)

    def tearDown(self):
        print("Test complete!")

if __name__ == "__main__":
    unittest.main()
