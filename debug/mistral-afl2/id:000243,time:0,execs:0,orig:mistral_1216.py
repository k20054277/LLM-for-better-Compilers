
# Import required modules
import os
from virtualenv import create_environment

# Create a new virtual environment
project_name = "my_project"
venv_path = os.path.join(os.getcwd(), project_name, "venv")
if not os.path.exists(venv_path):
    create_environment(venv_path, clear=True)
    print(f"Created new virtual environment: {venv_path}")

# Activate the virtual environment
activate_this = os.path.join(venv_path, "bin", "activate_this.py")
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Install a package (requests in this example)
os.system("pip install requests")

# Now import the package using 'as' keyword
import requests as req

# Use the imported package for some functionality
url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=API_KEY"
response = req.get(url)
data = response.json()
print(f"The temperature in London is {data['main']['temp']} degrees Celsius.")

# Deactivate the virtual environment
deactivate = os.path.join(venv_path, "bin", "deactivate")
os.system(deactivate)
