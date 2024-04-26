
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the dataframe
print(df)

# Filter the dataframe based on age and city
filtered_df = df[(df["Age"] >= 20) & (df["City"] == "Los Angeles")]

# Print the filtered dataframe
print(filtered_df)
