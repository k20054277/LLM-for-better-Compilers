import unittest

class TestExample(unittest.TestCase):
    def test_false(self):
        self.assertEqual(False, 0)

if __name__ == '__main__':
    unittest.main()