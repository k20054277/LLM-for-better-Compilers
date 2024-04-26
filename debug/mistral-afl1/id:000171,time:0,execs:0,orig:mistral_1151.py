
import pandas as pd

data = [['John', 20, 'Student'], ['Jane', 18, 'Teacher'], ['Mike', 23, 'Doctor']]

# Create a DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
print("Original DataFrame:")
print(df)
