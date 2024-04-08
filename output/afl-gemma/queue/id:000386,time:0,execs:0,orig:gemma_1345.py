
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.x = 10

    def tearDown(self):
        print("Tear down")

    def test_assert(self):
        self.assertEqual(self.x, 10)

    def test_with(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(self.x / 0, 0)

if __name__ == "__main__":
    unittest.main()
