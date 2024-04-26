import unittest

class TestAnd(unittest.TestCase):
    def test_and(self):
        self.assertTrue(True and True)
        self.assertFalse(True and False)
        self.assertFalse(False and True)
        self.assertFalse(False and False)

if __name__ == '__main__':
    unittest.main()