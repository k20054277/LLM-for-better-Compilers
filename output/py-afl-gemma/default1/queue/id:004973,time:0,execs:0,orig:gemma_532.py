
# Import os module to access environment variables
import os

# Define a None variable
my_none = None

# Print None
print("None value:", my_none)

# Access environment variable
my_env_var = os.getenv("MY_ENV_VAR")

# Print environment variable
print("Environment variable:", my_env_var)

# Check if environment variable is defined
if my_env_var is not None:
    print("Environment variable is defined")
else:
    print("Environment variable is not defined")
