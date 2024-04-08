
import resource
import unittest

class TestResource(unittest.TestCase):

    def setUp(self):
        self.original_mem_usage = resource.getmem()

    def tearDown(self):
        self.assertLessEqual(resource.getmem(), self.original_mem_usage)

    def test_memory_usage(self):
        # This line will cause the memory usage to increase
        large_list = [1] * 100000

        # Assert that the memory usage has increased
        self.assertGreater(resource.getmem(), self.original_mem_usage)

if __name__ == "__main__":
    unittest.main()
