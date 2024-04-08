
import unittest
import sys

class MyTest(unittest.TestCase):

    def setUp(self):
        self.my_obj = MyObject()

    def test_memory_usage(self):
        self.assertMemoryUsage(lambda: self.my_obj.consume_memory(), 10)

    def tearDown(self):
        del self.my_obj

class MyObject:

    def __init__(self):
        self.data = []

    def consume_memory(self):
        self.data.append(1)

if __name__ == "__main__":
    unittest.main()
