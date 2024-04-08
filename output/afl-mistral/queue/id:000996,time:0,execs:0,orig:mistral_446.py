
import os

# Using None
my_variable = None
print("Value of my_variable is:", my_variable)
if my_variable is not None:
    print("My variable has a value: ", my_variable)
else:
    print("My variable does not have a value.")

# Setting and getting environment variables
my_env_var = os.getenv('MYENVVAR')
print("\nValue of MYENVVAR environment variable is:", my_env_var)

if my_env_var is None:
    print("MYENVVAR environment variable does not have a value.")
else:
    print("MYENVVAR environment variable has the value: ", my_env_var)

# Setting an environment variable (for demo purpose, temporary change for this script session)
os.environ['ANOTHERENVVAR'] = 'AnotherValue'
another_env_var = os.getenv('ANOTHERENVVAR')
print("\nValue of ANOTHERENVVAR environment variable is:", another_env_var)
