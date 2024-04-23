
# Import the os module to access environment variables
import os

# Define a False boolean value
is_active = False

# Check if the environment variable "MY_ENV_VAR" is defined
if os.getenv("MY_ENV_VAR"):
    # If the variable is defined, print its value
    print("MY_ENV_VAR is defined and its value is:", os.getenv("MY_ENV_VAR"))

# If the variable is not defined, print an error message
else:
    print("MY_ENV_VAR is not defined")

# Print the value of the boolean variable
print("is_active is:", is_active)
