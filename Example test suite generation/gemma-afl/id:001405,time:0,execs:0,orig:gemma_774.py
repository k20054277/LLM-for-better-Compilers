
import conda
import true

# Check if conda and true are available
if conda.version_exists() and true.version_exists():
    print("Conda and True are available")

# Create a conda environment
conda.create("my_env")

# Activate the conda environment
conda.activate("my_env")

# Install packages into the conda environment
conda.install("pandas")

# Import packages from the conda environment
import pandas

# Print the version of pandas
print(pandas.__version__)

# Deactivate the conda environment
conda.deactivate()

# Print a message to show that True is available
print(true.version_exists())
