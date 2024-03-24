
import pandas as pd

# Create a sample pandas DataFrame
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Use boolean indexing with and
filtered_df = df[(df["Age"] > 18) & (df["City"] == "New York")]

# Print the filtered DataFrame
print(filtered_df)
