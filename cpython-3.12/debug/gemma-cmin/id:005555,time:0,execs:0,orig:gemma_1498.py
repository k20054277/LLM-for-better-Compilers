
import unittest
from virtualenv import VirtualEnv

# Create a virtual environment
venv = VirtualEnv('my_venv')
venv.create()

# Activate the virtual environment
venv.activate()

# Import the necessary libraries
import my_library

# Define a test case
class TestMyLibrary(unittest.TestCase):

    def setUp(self):
        self.my_library_obj = my_library.MyLibrary()

    def test_my_library_function(self):
        self.assertEqual(self.my_library_obj.my_function(), 10)

    def tearDown(self):
        venv.deactivate()

# Run the tests
unittest.main()
