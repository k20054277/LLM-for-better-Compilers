
# Importing required libraries
import pandas as pd

# Creating an empty DataFrame with given columns
data = {
    'Name': [None, "John", None],
    'Age': [None, 25, None],
    'City': ["New York", None, "Chicago"]
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Setting specific values to be None
df.loc[0, 'Name'] = None
df.loc[1, 'Age'] = None

# Displaying the updated DataFrame
print("\nUpdated DataFrame:")
print(df)
