
import pandas as pd

# Create a sample Pandas DataFrame
data = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the DataFrame
print(data)

# Accessing columns using as
pd_data = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})
print(pd_data["Name"])

# Iterating over rows using as
for row in pd_data.iterrows():
    print(row["Name"])

# Performing operations on columns using as
pd_data["Square"] = pd_data["Age"] ** 2
print(pd_data)
