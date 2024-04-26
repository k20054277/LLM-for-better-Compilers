# Create a new virtual environment using venv module
import venv

venv_name = "myenv"
venv.create(venv_name)

# Activate the virtual environment
activate_this = os.path.join(venv_name, "bin", "activate")
exec(open(activate_this).read(), dict(__file__=activate_this))

# Install the requests library in the virtual environment
!pip install requests

# Use the requests library in the virtual environment
import requests
response = requests.get("https://www.example.com")
print(response)

# Deactivate the virtual environment
!deactivate