import os

print("Current value of PATH:", os.environ["PATH"])

# Set a new value for the PATH environment variable
os.environ["PATH"] = "new_value"

print("New value of PATH:", os.environ["PATH"])