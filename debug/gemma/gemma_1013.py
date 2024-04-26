
import venv

# Create a virtual environment
venv.create('my_venv')

# Activate the virtual environment
venv.activate('my_venv')

# Install a package into the virtual environment
pip install pandas

# Import the package into the program
import pandas as pd

# Use the package to create a dataframe
df = pd.DataFrame({'Name': ['John Doe', 'Jane Doe', 'Peter Pan'], 'Age': [25, 30, 12], 'City': ['New York', 'Los Angeles', 'Neverland']})

# Print the dataframe
print(df)

# Deactivate the virtual environment
venv.deactivate()
