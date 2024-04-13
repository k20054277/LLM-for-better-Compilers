
import unittest

class Test(unittest.TestCase):

    def test_assert(self):
        self.assertEqual(10, 10)
        assert 10 == 10

    def test_try(self):
        try:
            self.assertEqual(10, 11)
        except Exception as e:
            self.assertEqual(e.__str__(), "AssertionError: Expected: 10, Actual: 11")

if __name__ == "__main__":
    unittest.main()
