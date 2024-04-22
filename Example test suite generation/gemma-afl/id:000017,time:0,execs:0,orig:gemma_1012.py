
# Install virtualenv and and packages
# pip install virtualenv and
# pip install pandas

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
venv/bin/activate

# Install pandas library inside the virtual environment
pip install pandas

# Import pandas library
import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the DataFrame
print(df)

# Deactivate the virtual environment
venv/bin/deactivate
