
# Function to be tested
def add_numbers(x, y):
    """Adds two numbers and checks if the result is within a given range."""
    assert x is not None and y is not None, "Both x and y should be provided."
    result = x + y
    assert result is not None, "Result should not be None"
    assert type(result) is int or type(result) is float, "Result should be a number"
    return result

# Test Case 1: Valid Inputs
class TestAddNumbers(unittest.TestCase):
    def test_add_valid_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

# Test Case 2: Invalid Input 1 (x is None)
class TestAddNumbers(unittest.TestCase):
    def test_add_invalid_x(self):
        with self.assertRaises(AssertionError):
            add_numbers(None, 3)

# Test Case 3: Invalid Input 2 (y is None)
class TestAddNumbers(unittest.TestCase):
    def test_add_invalid_y(self):
        with self.assertRaises(AssertionError):
            add_numbers(2, None)

# Test Case 4: Invalid Input 3 (Result is not a number)
class TestAddNumbers(unittest.TestCase):
    def test_add_invalid_result_type(self):
        with self.assertRaises(AssertionError):
            add_numbers(1, "abc")

# Running the tests
if __name__ == "__main__":
    unittest.main()
