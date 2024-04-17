import csv

# Open a CSV file
with open('data.csv', 'r') as f:
    # Create a reader object
    reader = csv.reader(f)
    # Iterate over the rows in the file
    for row in reader:
        # Check if any of the values are False
        if not any(value == False for value in row):
            # If none of the values are False, print the row
            print(row)