
import unittest
import virtualenv

# Create a virtual environment
virtualenv.create('my_venv')

# Activate the virtual environment
virtualenv.activate('my_venv')

# Import the necessary libraries
import sys
import my_library

# Define a test case
class TestMyLibrary(unittest.TestCase):

    def setUp(self):
        self.my_library_module = sys.modules['my_library']

    def test_my_function(self):
        self.assertEqual(self.my_library_module.my_function(10), 20)

    def tearDown(self):
        virtualenv.deactivate()

# Run the tests
unittest.main()
