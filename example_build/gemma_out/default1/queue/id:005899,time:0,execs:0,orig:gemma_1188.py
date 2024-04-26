
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({
    "name": ["John Doe", "Jane Doe", "Peter Pan"],
    "age": [30, 25, 12],
    "city": ["New York", "Los Angeles", "Neverland"]
})

# Print the dataframe
print(data)

# Accessing columns using the as keyword
name_as_col = data.as_columns("name")

# Print the modified dataframe
print(name_as_col)
