
import csv

# Open a CSV file
with open('data.csv') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Iterate over the remaining rows
    for row in reader:
        # Print the values of the row
        print(",".join(row))
