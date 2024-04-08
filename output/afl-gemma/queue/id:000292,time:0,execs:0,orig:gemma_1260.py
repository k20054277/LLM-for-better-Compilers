
# Import the necessary libraries
import os
import pip

# Define the requirements.txt file path
requirements_txt_path = "requirements.txt"

# Check if the requirements.txt file exists
if not os.path.isfile(requirements_txt_path):
    print("Error: requirements.txt file not found.")

# Otherwise, install the requirements
else:
    print("Installing dependencies...")
    pip install -r requirements.txt

    print("Dependencies installed successfully!")
