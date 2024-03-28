
import argparse

def process_file(input_file, output_file):
    """Reads data from input_file and writes it to output_file."""
    with open(input_file, 'r') as in_file:
        lines = in_file.readlines()

    with open(output_file, 'w') as out_file:
        for line in lines:
            out_file.write(line.strip().title())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process a file")
    input_arg = parser.add_argument("input", help="Input file to read from")
    output_arg = parser.add_argument("output", help="Output file to write to")

    args = parser.parse_args()

    process_file(args.input, args.output)
