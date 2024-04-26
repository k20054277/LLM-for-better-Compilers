
import os

def my_function():
    try:
        # This will raise an exception as 'myfile.txt' may not exist
        file = open('myfile.txt', 'r')
        data = file.read()
        print(data)
    except FileNotFoundError:
        # This block is executed when FileNotFoundError exception occurs
        print("File not found, creating a new one...")
        if not os.path.exists('myfile.txt'):
            with open('myfile.txt', 'w') as file:
                file.write("This is a new file.")
        else:
            print("The file already exists!")
    finally:
        # This block is executed regardless of the exception or successful execution
        if file is not None:
            file.close()
            print("File closed.")

my_function()
