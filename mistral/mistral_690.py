
# This script shows how to create a new Python virtual environment using venv,
# and then run a simple Python program within that environment.

import os
import sys

# Create a new virtual environment
print("Creating new virtual environment...")
venv_path = "my_project_env"
if not os.path.exists(venv_path):
    venv.create(sys.argv[0], venv_path, with_pip=True)
os.chdir(venv_path)

# Activate the virtual environment
print("Activating virtual environment...")
if sys.version_info >= (3, 3):
    import site

    site.activate(venv_path)
else:
    activate = os.path.join(venv_path, "bin", "activate")
    os.system(f"{activate} 'bash'")
    
# Now we can install and use packages within this environment
print("Installing requests package...")
try:
    import pip
    pip.main(["install", "requests"])
except Exception as e:
    print(f"Error installing requests: {e}")

# Demonstrate using True value
x = 10
y = 20
z = x + y
print("x = {}".format(x))
print("y = {}".format(y))
print("z = {}".format(z))
print("Is z greater than 15? {}".format(True if z > 15 else False))

# Deactivate the virtual environment
print("Deactivating virtual environment...")
deactivate = os.path.join(venv_path, "bin", "deactivate")
os.system(f"{deactivate}")
