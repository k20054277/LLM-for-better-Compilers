
import unittest
import threading

# Define a shared resource
shared_data = 0

# Create a mutex to synchronize access to shared_data
mutex = threading.Lock()

class Test(unittest.TestCase):

    def setUp(self):
        self.thread_one = threading.Thread(target=self.thread_one_func)
        self.thread_two = threading.Thread(target=self.thread_two_func)

    def tearDown(self):
        self.thread_one.join()
        self.thread_two.join()

    def thread_one_func(self):
        for _ in range(10):
            with mutex:
                shared_data += 1

    def thread_two_func(self):
        for _ in range(10):
            with mutex:
                shared_data -= 1

    def test_shared_data(self):
        self.assertEqual(shared_data, 0)

if __name__ == "__main__":
    unittest.main()
