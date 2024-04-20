import os
import subprocess

# Create a new directory
os.mkdir('my_directory')

# Assert that the directory was created successfully
assert os.path.exists('my_directory')

# Install a package using pip
subprocess.run(['pip', 'install', 'requests'])

# Assert that the package was installed successfully
assert subprocess.check_output(['pip', 'list']).decode().strip() == 'requests'