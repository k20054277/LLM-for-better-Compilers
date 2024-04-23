
import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description="Logical Conditions using argparse")

# Add arguments
parser.add_argument("arg1", help="First argument")
parser.add_argument("arg2", type=int, help="Second argument (must be an integer)")
parser.add_argument "--operation", "-o", type=str, required=True, help="Operation (+ or -)")

# Parse the arguments
args = parser.parse_args()

x = int(args.arg1)
y = args.arg2
operation = args.operation

if operation == "+":
    result = x + y
else:
    # only perform subtraction if the second argument is greater than the first one
    if x > y:
        result = y - x
    else:
        print("Error: Second argument must be greater than the first one")
        exit()

print(f"Result: {result}")
