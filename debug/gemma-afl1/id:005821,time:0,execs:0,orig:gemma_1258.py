
# Create a virtual environment
virtualenv venv

# Activate the virtual environment
venv/bin/activate

# Install python packages into the virtual environment
venv/bin/pip install pandas

# Import pandas library
import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the DataFrame
print(df)

# Deactivate the virtual environment
deactivate

# Print the DataFrame again (outside of the virtual environment)
print(df)
