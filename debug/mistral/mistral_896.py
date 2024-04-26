
import csv

# Function to validate if a given number is even
def is_even(number):
 if number % 2 == 0:
 return True
 else:
 return False

# Function to validate if a given string is empty or not
def is_empty_string(string):
 if len(string) > 0:
 return False
 else:
 return True

# Function to read data from CSV file
def read_csv(file_path):
 try:
 with open(file_path, newline='') as csvfile:
 reader = csv.DictReader(csvfile)
 data = [row for row in reader]
 return data
 except FileNotFoundError:
 print("File not found")
 return []

# Function to write data into CSV file
def write_csv(data, file_path):
 fieldnames = ['id', 'name', 'age']
 try:
 with open(file_path, mode='w', newline='') as csvfile:
 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 writer.writeheader()
 writer.writerows(data)
 print("CSV file has been written successfully.")
 except IOError:
 print("An error occurred while writing CSV file.")

# Sample data to write into CSV file
sample_data = [{'id': 1, 'name': 'John', 'age': 20}, {'id': 2, 'name': 'Jane', 'age': 30}]

# Write sample data into CSV file
write_csv(sample_data, "output.csv")

# Read data from CSV file and perform validation
data = read_csv("output.csv")

valid_records = []
for record in data:
 if not is_empty_string(record['name']) and is_even(int(record['age'])):
 valid_records.append(record)

# Print valid records
print(valid_records)
