
import unittest

# Function to be tested
def add(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):

    def test_add_two_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertIsEqual(add(2, 3), 5)

    def test_add_two_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertIsEqual(add(-2, -3), -5)

    def test_add_positive_and_zero(self):
        """Test adding a positive number and zero."""
        self.assertIsEqual(add(4, 0), 4)

    def test_add_zero_and_positive(self):
        """Test adding zero and a positive number."""
        self.assertIsEqual(add(0, 4), 4)

    def test_add_two_large_numbers(self):
        """Test adding two large numbers."""
        self.assertIsEqual(add(100, 200), 300)

if __name__ == '__main__':
    unittest.main()
