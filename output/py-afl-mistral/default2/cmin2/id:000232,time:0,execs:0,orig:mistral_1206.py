
# Function to open a file and read its content
def open_and_read_file(filename):
    try:
        file = open(filename, "r")  # Attempt to open the file
        content = file.read()       # Read the entire content
    except FileNotFoundError as e:
        print(f"File '{filename}' was not found!")
        return None
    finally:
        if file:
            file.close()          # Close the file even if an exception occurred
    return content

# Function to process the data read from a file
def process_data(data):
    try:
        result = int(data)  # Attempt to convert the data to integer
    except ValueError as e:
        print("Invalid data format!")
        return None
    return result * 2  # Process the data by doubling its value

if __name__ == "__main__":
    filename = "example.txt"
    content = open_and_read_file(filename)
    if content is not None:
        result = process_data(content)
        print(f"The processed data: {result}")
