import os

# Define a variable with the value "None"
none_var = None

# Print the type of the variable
print(type(none_var)) # Output: <class 'NoneType'>

# Use conda.yml to install the required packages
with open("conda.yml", "r") as f:
    env = yaml.safe_load(f)
    conda.install(env)