import unittest

class TestBool(unittest.TestCase):
    def test_false(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()