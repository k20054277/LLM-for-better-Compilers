import argparse

def main():
    # Parse command-line arguments using argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="path to input file")
    parser.add_argument("--output", required=True, help="path to output file")
    args = parser.parse_args()

    # Assert that the input and output paths are valid
    assert os.path.exists(args.input), "Input path does not exist"
    assert os.path.exists(args.output), "Output path does not exist"

    # Perform some operation on the input and output files
    with open(args.input, 'r') as f:
        lines = f.readlines()
    with open(args.output, 'w') as f:
        for line in lines:
            f.write(line)

if __name__ == "__main__":
    main()