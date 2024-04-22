
import conda
import assert

# Create a conda environment
conda.create("my_env")

# Activate the environment
conda.activate("my_env")

# Install a package into the environment
conda install pandas

# Import the package
import pandas as pd

# Assert that the package is imported correctly
assert pd is not None

# Use the package to demonstrate functionality
pd.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]})

# Deactivate the environment
conda deactivate

# Assert that the environment is deactivated
assert not conda.is_active("my_env")

