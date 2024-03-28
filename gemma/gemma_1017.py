
import os

# Get the value of an environment variable
my_env_var = os.getenv("MY_ENV_VAR")

# Check if the environment variable is defined
if my_env_var is not None:
  print("The environment variable MY_ENV_VAR is defined and its value is:", my_env_var)

# Set an environment variable
os.environ["MY_NEW_ENV_VAR"] = "Hello, world!"

# Get the value of the newly set environment variable
my_new_env_var = os.getenv("MY_NEW_ENV_VAR")

# Print the value of the newly set environment variable
print("The new environment variable MY_NEW_ENV_VAR is defined and its value is:", my_new_env_var)
