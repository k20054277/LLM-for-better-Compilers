#!/usr/bin/env python

# This line imports the necessary libraries to run this script
import sys, os

# This line sets up the virtual environment using the "venv" module
venv = sys.modules['venv']
venv.create('my_virtualenv', with_pip=True)

# This line installs a package in the virtual environment
venv.install('requests')

# This line imports the package we just installed
import requests

# This line uses the package to make an HTTP request
response = requests.get('https://www.example.com')

# This line checks if the response was successful (i.e., has a status code of 200)
if response.status_code == 200:
    print("Success!")
else:
    print("Failed.")