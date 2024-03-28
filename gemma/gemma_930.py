
import pandas as pd

# Read a CSV file
df = pd.read_csv('example.csv')

# Print the head of the DataFrame
print(df.head())

# Filter the data using AND condition
filtered_df = df[(df['age'] > 18) & (df['gender'] == 'male')]

# Print the filtered DataFrame
print(filtered_df)
