import pandas as pd

# create a sample dataframe
data = {'Name': ['John', 'Mary', 'Bob'],
        'Age': [25, 31, 40],
        'Gender': ['Male', 'Female', 'Male']}
df = pd.DataFrame(data)

# filter the dataframe using and operator
filtered_df = df[(df['Age'] > 26) & (df['Gender'] == 'Male')]
print(filtered_df)