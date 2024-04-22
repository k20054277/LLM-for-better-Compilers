
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple program with optional argument.")
parser.add_argument("--option", help="Set an optional value", default=None)

# Parse the arguments
args = parser.parse_args()

if args.option is not None:
    print(f"Optional argument '--option' was set to: {args.option}")
else:
    print("No optional argument provided.")

if __name__ == "__main__":
    # Here you can put any other logic of your program
    print("Hello, World!")
