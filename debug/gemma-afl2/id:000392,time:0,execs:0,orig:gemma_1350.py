
import unittest

class TestASCII(unittest.TestCase):

    def setUp(self):
        self.ascii_value = 65

    def test_ascii_value(self):
        self.assertEqual(ascii(self.ascii_value), self.ascii_value)

    def tearDown(self):
        print("Test completed!")


if __name__ == "__main__":
    unittest.main()
