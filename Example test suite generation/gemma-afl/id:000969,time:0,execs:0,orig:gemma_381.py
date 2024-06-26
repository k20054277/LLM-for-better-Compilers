
import csv

# Define a list of data
data = [
    ["John Doe", 30, "New York"],
    ["Jane Doe", 25, "Los Angeles"],
    ["Peter Pan", 12, "Neverland"]
]

# Create a CSV writer object
with open("data.csv", "w") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(["Name", "Age", "City"])

    # Write the data rows
    writer.writerows(data)

# Print the contents of the CSV file
with open("data.csv") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)

# Output:
# ['Name', 'Age', 'City']
# ['John Doe', '30', 'New York']
# ['Jane Doe', '25', 'Los Angeles']
# ['Peter Pan', '12', 'Neverland']
