
# Importing the required module for file handling
import io

def open_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        data = file.read()
        file.close()
        return data
    except FileNotFoundError as e:
        print("File not found error:", str(e))
        return None
    except Exception as e:
        print("An unexpected error occurred:", str(e))
        return None

# Using the open_file function with a valid file name
data = open_file('example.txt')
if data is not None:
    print("Data read from the file:")
    print(data)

# Using the open_file function with an invalid file name
data = open_file('non-existent.txt')
