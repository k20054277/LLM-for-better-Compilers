import yaml

# Load the conda environment file
with open('conda.yml') as f:
    env = yaml.load(f)

# Check if the environment is installed
if env['name'] in conda_list():
    print("The environment is installed.")
else:
    print("The environment is not installed.")

# Install the environment
if not env['name'] in conda_list():
    conda.install(env)
    print("Environment installed successfully!")