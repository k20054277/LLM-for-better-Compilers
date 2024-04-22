
import csv

# Replace 'filename.csv' with the actual path or name of your CSV file
filename = "filename.csv"

def is_non_empty_string(value):
"""
Helper function to check if a value is a non-empty string
"""
return isinstance(value, str) and len(value) > 0

with open(filename, newline='') as csvfile:
reader = csv.DictReader(csvfile)

print("First row of the CSV file as a dictionary with True values for non-empty columns:")
for row in itertools.islice(reader, 1):
column_values = {col: bool(is_non_empty_string(value)) for col, value in row.items()}
print(column_values)
break
