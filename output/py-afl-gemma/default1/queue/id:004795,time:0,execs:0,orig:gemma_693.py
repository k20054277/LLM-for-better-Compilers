
import csv

# Define a list of data
data = [
    {"name": "John Doe", "age": 30, "occupation": "Software Engineer"},
    {"name": "Jane Doe", "age": 25, "occupation": "Teacher"},
    {"name": "Peter Pan", "age": 12, "occupation": "Student"}
]

# Create a CSV writer
writer = csv.writer(open("data.csv", "w"))

# Write the header row
writer.writerow(["name", "age", "occupation"])

# Write the data rows
writer.writerows(data)

# Print the CSV file
print("Data written to data.csv")
