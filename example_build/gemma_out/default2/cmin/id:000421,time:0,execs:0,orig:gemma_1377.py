
import unittest

class TestClass(unittest.TestCase):

    def setUp(self):
        self.a = 10

    def test_assert(self):
        self.assertGreater(self.a, 5)

    def test_id(self):
        self.assertEqual(id(self), id(self))

if __name__ == "__main__":
    unittest.main()
