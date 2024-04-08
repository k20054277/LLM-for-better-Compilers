import os
from virtualenv import create_environment

# Create a new virtual environment with name "my_env"
create_environment('my_env')

# Activate the virtual environment
os.system("source my_env/bin/activate")

# Print the current path to demonstrate that we are now in the virtual environment
print(os.getcwd())

# Create a new file called "test.py" with some code
with open('test.py', 'w') as f:
    f.write("print('Hello from test.py!')")

# Run the code in the virtual environment using the `as` command
os.system("python -m as my_env test.py")