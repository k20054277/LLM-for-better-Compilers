
import csv

# Create an empty list to store rows for a CSV file
rows = []

# Function to add a row to the list, with an optional value for the last column
def add_row(rows, *args):
 if len(args) > len(rows[-1] if rows else (0,)):
 # If new columns are being added, create a new list with more columns
 rows.append([None] * (len(args) - len(rows[-1] if rows else 0) + len(rows[-1] if rows else 0))

 # Add the non-None values to the row
 args += [None] * (len(rows[-1]) if rows else 0 - len(args))
 rows[-1] += args[len(args) - len(rows[-1]):]

 # Overwrite the last value with the new one, if provided
 if len(args) > len(rows[-1]):
 rows[-1][-1] = args[-1]

 # Add None to the rest of the columns if they are not provided
 for i in range(len(rows[-1]) - 1):
 if i >= len(args):
 rows[-1][i] = None
 add_row(rows, 'Name', 25)
 add_row(rows, 'Age', 30)
 add_row(rows, 'City', 'New York')
 add_row(rows, 'Country', 'USA')

# Write the data to a CSV file
with open('output.csv', mode='w', newline='') as file:
 csv_writer = csv.writer(file)
 csv_writer.writerows(rows)

# Print the content of the CSV file
with open('output.csv', 'r') as file:
 print(file.read())
