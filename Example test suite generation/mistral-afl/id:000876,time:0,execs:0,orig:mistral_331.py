
# Function to write data into a file
def write_data_to_file(filename, data):
    try:
        with open(filename, 'w') as file:
            if data is None:
                print("Data is None. Skipping file write.")
            else:
                file.write(data)
                print("Data written to file successfully.")
    except FileNotFoundError:
        print("File does not exist. Creating new file with default data...")
        with open(filename, 'w') as new_file:
            new_file.write("Default data")

# Call the function with some data or None
write_data_to_file("example.txt", "Hello World!")
write_data_to_file("nonexistent_file.txt", None)
