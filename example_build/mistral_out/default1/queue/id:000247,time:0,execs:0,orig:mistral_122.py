
# Import pandas library
import pandas as pd

# Create a simple DataFrame with boolean values
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Active': [True, False, True]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Set some values to be False
df.loc[1, 'Active'] = False

print("\nDataFrame after setting 'Bob's Active value to False:")
print(df)

# Use boolean indexing and filtering
bool_index = df['Active'].values
mask = df['Name'] == 'Alice'
selected_rows = df[mask]

print("\nSelected rows with Active = True:")
print(df[df['Active']])

print("\nSelected row with Name = 'Alice':")
print(selected_rows)
