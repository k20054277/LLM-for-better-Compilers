
# Define an environment variable
my_env_var = "Hello, world!"

# Use the environment variable in a print statement
print("The value of the environment variable is:", my_env_var)

# Access the environment variable using the as keyword
with env_var:
    print("The value of the environment variable is:", env_var)

# Print the value of the environment variable after the with statement
print("The value of the environment variable is:", my_env_var)
