
import pandas as pd

# Create a Pandas dataframe
df = pd.DataFrame({"name": ["John Doe", "Jane Doe", "Peter Pan"], "age": [30, 25, 12], "city": ["New York", "Los Angeles", "Neverland"]})

# Print the dataframe
print(df)

# Accessing a specific column
print(df["name"])

# Iterating over the rows of the dataframe
for i, row in df.iterrows():
    print(row["name"])

# Using the as keyword to assign a different name to the Pandas class
pd_alt = pandas

# Print the dataframe using the alternative name
print(pd_alt.DataFrame({"name": ["John Doe", "Jane Doe", "Peter Pan"], "age": [30, 25, 12], "city": ["New York", "Los Angeles", "Neverland"]}))
