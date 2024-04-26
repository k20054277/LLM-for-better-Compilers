
import os

# Define an environment variable
my_env_var = os.getenv("MY_ENV_VAR")

# Assert that the environment variable is defined
assert my_env_var is not None

# Assert that the environment variable is equal to "my value"
assert my_env_var == "my value"

# Print the environment variable
print("My environment variable is:", my_env_var)
