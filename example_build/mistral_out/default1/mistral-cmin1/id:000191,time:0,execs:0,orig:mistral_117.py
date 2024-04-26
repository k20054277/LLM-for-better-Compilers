
import argparse

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="A simple Python program")

    # Add some arguments with default values and optional descriptions
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("--quiet", action="store_false", dest="verbose", help="Decrease output verbosity (default)")
    parser.add_argument("input", help="The input file to process")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Print the parsed arguments and their boolean flags
    print(f"Input: {args.input}")
    print(f"Verbose mode: {'True' if args.verbose else 'False'}")
    print(f"Quiet mode: {'True' if not args.quiet else 'False'}")

if __name__ == "__main__":
    main()
