
import os

# Define the name of the environment variable to check
env_variable_name = "MYVAR"

if os.environ.get(env_variable_name, False):
    # If the environment variable is defined, print a message
    value = os.environ[env_variable_name]
    print(f"Environment variable '{env_variable_name}' is set to '{value}'")
else:
    # If the environment variable is not defined or empty, print a different message
    print(f"Environment variable '{env_variable_name}' is not set")

# Print a message showing that 'True' is equivalent to any non-empty value
print("True if any non-empty string:")
if os.environ.get(env_variable_name, True):
    print(f"'{os.environ.get(env_variable_name, '')}' is truthy")
else:
    print("'None' or an empty string is falsy")
