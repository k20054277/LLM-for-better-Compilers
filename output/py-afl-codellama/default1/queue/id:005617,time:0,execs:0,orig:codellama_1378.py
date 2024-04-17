# Define a function that takes two numbers as input and returns their sum
def add(x, y):
    return x + y

# Import the unittest module
import unittest

# Create a new class that inherits from the unittest.TestCase class
class TestAdd(unittest.TestCase):
    
    # Define a test method for the add function
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# Run the test case
if __name__ == '__main__':
    unittest.main()