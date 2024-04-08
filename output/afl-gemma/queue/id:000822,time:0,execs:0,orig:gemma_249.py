
import pandas as pd

# Read CSV file
df = pd.read_csv('example.csv')

# Print the head of the DataFrame
print(df.head())

# Filter rows where the value in the 'age' column is greater than 18
filtered_df = df[df['age'] > 18]

# Print the head of the filtered DataFrame
print(filtered_df.head())

# Export the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_example.csv', index=False)
