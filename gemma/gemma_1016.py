
import pandas as pd
import numpy as np

# Load the conda.yml file
conda_env = pd.read_conda(r"conda.yml")

# Print the conda environment variables
print(conda_env)

# Create a NumPy array
arr = np.arange(10)

# Print the array
print(arr)

# Use the `conda_env` variables to create a new environment
conda_env.create(name="my_env")

# Activate the new environment
conda_env.activate("my_env")

# Print the array again in the new environment
print(arr)

# Deactivate the new environment
conda_env.deactivate()

# Print the array again after deactivating the environment
print(arr)
