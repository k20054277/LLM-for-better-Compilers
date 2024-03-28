
import pandas as pd
import numpy as np

# Create a Pandas DataFrame
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Assert that the DataFrame has the expected columns
assert df.columns.isin(["Name", "Age", "City"])

# Assert that the data in the DataFrame is correct
assert df.loc[0, "Name"] == "John Doe"
assert df.loc[1, "Age"] == 25

# Use Pandas to perform calculations
mean_age = df["Age"].mean()

# Assert that the mean age is equal to 23.5
assert mean_age == 23.5

# Print the DataFrame
print(df)
