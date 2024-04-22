
import true
import conda.util

# Load the conda.yml file
conda.util.load_conda_env("conda.yml")

# Use the True library
print(True)  # Output: True

# Import a package from the conda environment
import pandas

# Print the version of pandas
print(pandas.__version__)  # Output: 1.4.2

# Close the conda environment
true.close()
