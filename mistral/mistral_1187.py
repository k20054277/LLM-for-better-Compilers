
class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

if __name__ == "__main__":
    file_handler = FileHandler("example.txt")

    # Use the file object with 'as' and assign it to a variable
    with file_handler as f:
        content = f.readline()
        print(content)

    # Access return value of a function using 'return' statement
    def square(number):
        result = number ** 2
        return result

    number = 3
    squared_number = square(number)
    print(squared_number)
