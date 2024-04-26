
import os
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.temp_dir = os.path.join(os.path.dirname(__file__), "temp")
        os.mkdir(self.temp_dir)

    def tearDown(self):
        os.rmdir(self.temp_dir)

    def test_assert(self):
        self.assertEqual(10, 10)
        self.assertTrue(True)
        self.assertFalse(False)

    def test_os(self):
        self.assertEqual(os.path.exists(self.temp_dir), True)
        self.assertEqual(os.path.basename(self.temp_dir), "temp")

if __name__ == "__main__":
    unittest.main()
