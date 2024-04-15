import os

def main():
    # Use assert to check if the input file exists
    assert os.path.exists("input.txt"), "Input file does not exist"

    # Open the input file for reading
    with open("input.txt", "r") as f:
        # Read the contents of the file
        data = f.read()

    # Use assert to check if the output file exists
    assert os.path.exists("output.txt"), "Output file does not exist"

    # Open the output file for writing
    with open("output.txt", "w") as f:
        # Write the contents of the file
        f.write(data)

if __name__ == "__main__":
    main()