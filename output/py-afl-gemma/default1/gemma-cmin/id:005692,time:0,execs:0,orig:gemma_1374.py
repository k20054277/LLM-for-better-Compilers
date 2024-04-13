
import unittest

class TestHash(unittest.TestCase):

    def setUp(self):
        self.my_dict = {"a": 1, "b": 2, "c": 3}

    def test_hash(self):
        self.assertEqual(hash(self.my_dict), 111011)

    def test_assert(self):
        self.assertGreater(self.my_dict["a"], 0)
        self.assertTrue("c" in self.my_dict)

if __name__ == "__main__":
    unittest.main()
