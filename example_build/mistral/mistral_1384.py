
import csv

# Function to read CSV file and process its content using assertions
def process_csv_file(filename):
    # Open CSV file in read mode
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Process each row in the CSV file using assert statements
        for row in reader:
            # Assert that all values in a row have expected keys
            assert 'key1' in row and 'key2' in row, \
                f"Missing expected keys {'key1'} or {'key2}' in row: {row}"
            
            # Assert that value of 'key1' is an integer
            assert isinstance(row['key1'], int), \
                f"Value of key 'key1' in row '{row}' is not an integer: {row['key1']}"

            # Assert that value of 'key2' is a float within expected range
            assert 0.0 <= float(row['key2']) <= 10.0, \
                f"Invalid value of key 'key2' in row '{row}': {row['key2']}"
            
# Function to write processed data back to CSV file
def write_processed_data(filename, data):
    # Open CSV file in write mode with newline delimiter
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['key1', 'key2'])

        # Write the processed data to the CSV file
        writer.writeheader()
        writer.writerows([{'key1': i, 'key2': str(f * 2)} for i, f in data])

# Sample usage: Process and write back data from a sample CSV file
if __name__ == "__main__":
    filename = "sample_data.csv"
    process_csv_file(filename)

    # Generate some sample processed data
    data = [(i, f * 2) for i, f in ((1, 3), (2, 4), (3, 6))]

    write_processed_data(filename, data)
