
# Import the as and virtualenv modules
import as
import virtualenv

# Create a virtual environment
virtualenv.create('my_venv')

# Activate the virtual environment
as 'my_venv'

# Install pip packages
pip install pandas

# Use pip packages
import pandas as pd

# Print a Pandas dataframe
pd.DataFrame({"Name": ["John Doe", "Jane Doe"], "Age": [30, 25], "City": ["New York", "Los Angeles"]}).to_console()

# Deactivate the virtual environment
deactivate

# Print the output
print("The Pandas dataframe has been printed.")
