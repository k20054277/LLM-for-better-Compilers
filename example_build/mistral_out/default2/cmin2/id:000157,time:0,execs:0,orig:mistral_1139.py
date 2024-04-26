
import csv

# Specify the file path or file object
file_path = "example.csv"

with open(file_path, newline="") as csvfile:
    # Create a CSV reader object
    reader = csv.DictReader(csvfile)

    # Loop through each row and print the keys and values
    for row in reader:
        print(row.keys())
        print(row.values())
        print("--------------------")

# Output will be something like this:
# {'Name': 'John Doe', 'Age': '30', 'City': 'New York'}
# {'Name': 'Jane Doe', 'Age': '28', 'City': 'Chicago'}
# --------------------
