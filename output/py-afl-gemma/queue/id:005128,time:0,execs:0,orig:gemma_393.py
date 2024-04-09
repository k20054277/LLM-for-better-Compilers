
import pandas as pd

# Define a False boolean value
false_bool = False

# Create a pandas DataFrame
df = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})

# Check if the value False is equal to the boolean False
print(false_bool == False)  # Output: True

# Filter rows where the value in column "A" is greater than 2
print(df[df["A"] > 2])  # Output:   
#   A  B
# 2  3  c
