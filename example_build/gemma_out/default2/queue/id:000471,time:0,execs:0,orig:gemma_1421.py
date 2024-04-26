
import csv
import assert

# Define a CSV file name
csv_file_name = "example.csv"

# Open the CSV file
with open(csv_file_name) as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Assert the header row is as expected
    assert next(csvreader) == ["Name", "Age", "City"]

    # Assert the data row is as expected
    assert next(csvreader) == ["John Doe", 30, "New York"]
    assert next(csvreader) == ["Jane Doe", 25, "Los Angeles"]

    # Assert the CSV file has the expected number of rows
    assert len(list(csvreader)) == 3
