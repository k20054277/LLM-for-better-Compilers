
import os

# Get the value of an environment variable, if it exists
MY_ENV_VAR = os.getenv('MY_ENV_VAR', 'Default value')

print(f'The value of environment variable MY_ENV_VAR is: {MY_ENV_VAR}')

if __name__ == '__main__':
    # Set an environment variable for this script only (effective for the current process)
    os.environ['ANOTHER_ENV_VAR'] = 'Some value'
    
    another_env_var = os.getenv('ANOTHER_ENV_VAR')
    print(f'The value of environment variable ANOTHER_ENV_VAR is: {another_env_var}')
