
import pandas as pd

# Create a simple DataFrame
data = {'Name': ['John', 'Anna', 'Peter'],
       'Age': [28, 24, 35],
       'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Perform some data manipulation using pandas
df['Gender'] = ['M' for _ in df.index]
df = df.rename(columns={'Age': 'Ages'})

# Function to validate DataFrame
def validate_dataframe(dataframe):
    assert len(dataframe) > 0, "DataFrame is empty"
    assert all(dataframe['Name'].notnull()), "Missing names in DataFrame"
    assert all(dataframe['Ages'].apply(lambda x: type(x) == int)), "Age column should be of integer type"

# Validate the DataFrame
validate_dataframe(df)

# Demonstrating an assertion failure
# df.loc[0, 'Name'] = None  # Uncomment this line to trigger an assertion error

print(df)
