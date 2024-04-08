import csv

# Open a CSV file with headers
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)

    # Read the first row
    row = next(reader)

    # Print the value of the "name" column for the first row
    print(row['name'])