
import unittest

# Define a function to demonstrate assert and lock
def my_function(lock):
    with lock:
        assert 10 == 10
        print("Function executed successfully!")

# Create a lock object
lock = threading.Lock()

# Create a test case
class TestMyFunction(unittest.TestCase):

    def setUp(self):
        self.lock = lock

    def test_my_function(self):
        my_function(self.lock)

# Run the tests
unittest.main()
