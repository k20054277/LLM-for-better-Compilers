# Create a new virtual environment
python -m venv myenv

# Activate the virtual environment
myenv\Scripts\activate.bat

# Check that you are in the virtual environment
python -c "import sys; print(sys.executable)"

# Install a package using pip
pip install requests

# Use the package
import requests
response = requests.get("https://www.example.com")
print(response.status_code)

# Exit the virtual environment
deactivate