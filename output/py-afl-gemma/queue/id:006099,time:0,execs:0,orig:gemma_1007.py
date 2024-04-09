
# Create a virtual environment
virtualenv venv

# Activate the virtual environment
venv/bin/activate

# Install the required packages
pip install pandas

# Import the pandas library
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [25, 30, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the dataframe
print(df)

# Deactivate the virtual environment
venv/bin/deactivate
