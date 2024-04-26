
import pandas as pd
import conda

# Create a conda environment
conda create --name my_env python=3.8 pandas

# Activate the conda environment
conda activate my_env

# Import pandas library
import pandas as pd

# Create a pandas dataframe
df = pd.DataFrame({"name": ["John Doe", "Jane Doe", "Peter Pan"], "age": [30, 25, 12], "city": ["New York", "Los Angeles", "Neverland"]})

# Print the dataframe
print(df)

# Deactivate the conda environment
conda deactivate

# Print the dataframe again (outside of the environment)
print(df)
