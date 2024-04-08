try:
    with open("example_file.txt", "r") as file:
        contents = file.read()
except OSError as e:
    print(f"Error reading file: {e}")
except ValueError as e:
    print(f"Invalid value in file: {e}")