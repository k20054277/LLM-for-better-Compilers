
import csv

# Assume we have a CSV file named "data.csv" in the same directory as this script
file_path = "data.csv"

# Initialize an empty list to store our data
data = []

try:
    # Open the CSV file with 'r' mode, which stands for read-only
    with open(file_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        
        # Check if there are any rows in the CSV file (i.e., if it is empty)
        header = next(reader, False)
        data = list(reader) if header else data

except FileNotFoundError:
    print("File not found!")

if len(data) == 0:
    print("CSV file is empty.")
else:
    print("CSV file contains the following data:")
    for row in data:
        print(row)

# Close the 'False' statement, which was opened implicitly when using 'try'
finally:
    # Close the CSV file (even if there was an error)
    with open(file_path, "r", newline="") as csvfile:
        csvfile.close()
