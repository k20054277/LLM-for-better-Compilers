
import pandas as pd

# Create a dictionary
data = {"name": ["John Doe", "Jane Doe", "Peter Pan"], "age": [30, 25, 12], "city": ["New York", "Los Angeles", "Neverland"]}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Check if a condition is true
is_true = df["age"] > 18

# Print the rows where the condition is true
print(df[is_true])

# True and False values
print(True and False)
