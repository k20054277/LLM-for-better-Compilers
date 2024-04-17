import csv

# Open the CSV file
with open('example.csv', 'r') as f:
    # Create a dictionary reader
    reader = csv.DictReader(f)
    
    # Iterate over the rows in the file
    for row in reader:
        # If the value of the "active" column is True, print the row
        if row['active'] == 'True':
            print(row)