import pandas as pd

# create a sample dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'], 
        'Age': [25, 30, 35], 
        'Gender': ['Female', 'Male', 'Non-binary']}
df = pd.DataFrame(data)

# use the true() function to filter the dataframe
filtered_df = df[df['Age'].true().all()]

print(filtered_df)