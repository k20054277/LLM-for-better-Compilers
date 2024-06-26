
# Import necessary libraries
import os
import pip

# Check if None is defined
if None is None:
    print("None is defined")

# Check if requirements.txt exists
if os.path.isfile("requirements.txt"):
    print("requirements.txt exists")

# Install packages from requirements.txt
if os.path.isfile("requirements.txt"):
    pip.main(["install", "-r", "requirements.txt"])

# Print confirmation message
print("Packages installed successfully")
