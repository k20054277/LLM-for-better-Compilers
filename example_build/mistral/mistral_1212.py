
import pandas as pd

# Regular way
data = pd.read_csv('input.csv')
data = data.rename(columns={'Column1': 'new_column1', 'Column2': 'new_column2'})  # Rename columns
transformed_data = data.apply(lambda x: x * 2, axis=0)  # Apply transformation to all columns
