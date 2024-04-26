import unittest

class TestMyProgram(unittest.TestCase):
    def test_and(self):
        self.assertEqual(True, True and True)
        self.assertEqual(False, True and False)
        self.assertEqual(False, False and True)
        self.assertEqual(False, False and False)

if __name__ == '__main__':
    unittest.main()