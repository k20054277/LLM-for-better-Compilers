
# Import necessary libraries
import unittest

# Define a class for testing
class TestClass(unittest.TestCase):

    # Define a method to test the functionality
    def test_list(self):
        # Create a list
        my_list = [1, 2, 3, 4, 5]

        # Assert that the length of the list is 5
        self.assertEqual(len(my_list), 5)

        # Assert that the elements of the list are in ascending order
        self.assertTrue(sorted(my_list) == my_list)

# Run the tests
if __name__ == "__main__":
    unittest.main()
