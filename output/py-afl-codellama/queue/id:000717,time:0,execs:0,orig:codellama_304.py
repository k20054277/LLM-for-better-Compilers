import subprocess

# Creating a new virtual environment named "myenv"
subprocess.run(["python", "-m", "venv", "myenv"])

# Activating the virtual environment
subprocess.run(["source", "myenv/bin/activate"])

# Installing the requests library in the virtual environment
subprocess.run(["pip", "install", "requests"])

# Using the requests library to make a HTTP request
import requests
response = requests.get("https://www.example.com")

# Printing the status code of the response
print(response.status_code)

# Deactivating the virtual environment
subprocess.run(["deactivate"])