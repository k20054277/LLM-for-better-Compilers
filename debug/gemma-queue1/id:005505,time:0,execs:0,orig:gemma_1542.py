
import unittest

class TestAssert(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert_equal(self):
        self.assertEqual(self.a, 10)

    def test_assert_not_equal(self):
        self.assertNotEqual(self.a, 11)

    def test_assert_greater_than(self):
        self.assertGreater(self.a, 9)

    def test_assert_less_than(self):
        self.assertLess(self.a, 12)

    def tearDown(self):
        print("Test completed!")

if __name__ == "__main__":
    unittest.main()
