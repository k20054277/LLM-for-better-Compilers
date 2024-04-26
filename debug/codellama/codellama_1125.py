import sys

def main():
    # Get the command line arguments
    args = sys.argv[1:]

    # Print the usage message
    print("Usage: python example.py <input_file>")

    # Check if there are any input files
    if len(args) == 0:
        return

    # Get the first input file
    input_file = args[0]

    # Read the contents of the input file
    with open(input_file, "r") as f:
        data = f.read()

    # Print the contents of the input file
    print("Contents of", input_file)
    print(data)

if __name__ == "__main__":
    main()