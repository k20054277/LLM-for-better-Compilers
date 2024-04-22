
import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [30, 25, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the DataFrame
print(df)

# Filter the DataFrame by age and city
filtered_df = df[(df["Age"] > 20) & (df["City"] == "Los Angeles")]

# Print the filtered DataFrame
print(filtered_df)
