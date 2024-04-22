
import as
import conda

# Use as to create a shortcut for the as module
as_ = as.module()

# Use conda to create a new environment
conda_env = conda.create("my_env")

# Activate the environment
conda_env.activate()

# Use the as module to import libraries from the environment
import numpy as np

# Print the version of numpy in the environment
print(np.__version__)

# Deactivate the environment
conda_env.deactivate()
