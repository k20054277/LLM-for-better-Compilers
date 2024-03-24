import csv

# Create a CSV file with a single row
with open('example.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Alice', 'age': 25})

# Read the CSV file and print its contents
with open('example.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'])

# Update the age field of the first row to 30
with open('example.csv', 'r+', newline='') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['name'] == 'Alice':
            row['age'] = 30
    writer.writerow(row)