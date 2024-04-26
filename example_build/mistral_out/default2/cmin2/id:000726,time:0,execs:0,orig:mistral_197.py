
import os

# Set default value of env_variable to be False
env_variable = False

# Check if the environment variable MYVAR is set, and if so, set it to True
if 'MYVAR' in os.environ:
    env_variable = os.environ['MYVAR']
    if env_variable == '':
        print('Environment variable is set but empty.')
    else:
        try:
            env_variable = bool(env_variable)
            if not env_variable:
                print('Environment variable is set but its value is False.')
        except ValueError:
            print(f'Environment variable {env_variable} is not a valid boolean value.')
else:
    print('Environment variable MYVAR is not set.')

# Demonstrate the usage of False
if not 5 > 4:
    print('Five is not greater than four, which is false.')
if not env_variable:
    print('env_variable is False.')
