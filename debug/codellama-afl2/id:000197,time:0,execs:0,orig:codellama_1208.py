import os

# Create a new environment using Anaconda
os.system("conda create --name myenv")

# Activate the environment
os.system("conda activate myenv")

# Install a package in the environment
os.system("conda install requests")

# Deactivate the environment
os.system("conda deactivate")