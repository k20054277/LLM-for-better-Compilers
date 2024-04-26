
import conda
import numpy as np

# Create a conda environment
conda.create('my_env', python='3.7', notebook='jupyter')

# Activate the conda environment
conda.activate('my_env')

# Import numpy in the conda environment
np.arange(10)

# Print the numpy array
print(np.arange(10))

# Deactivate the conda environment
conda.deactivate()
