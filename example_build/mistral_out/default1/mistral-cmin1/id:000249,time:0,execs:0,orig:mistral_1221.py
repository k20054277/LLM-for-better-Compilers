
# my_script.py

# Create a new virtual environment and activate it
import subprocess

virtualenv_path = "my_venv"
subprocess.check_call([sys.executable, "-m", "virtualenv", virtualenv_path])
subprocess.check_call([sys.executable, "--no-site-packages", "--reuse-root", ".", virtualenv_path + "/bin/activate"])

# Install a package using pip
subprocess.check_call(["pip", "install", "requests"])

import requests as req

# Use the imported 'requests' module
response = req.get("https://www.example.com")
print(response.status_code)
