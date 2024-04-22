
import argparse
import assert

# Define a function to demonstrate assert and argparse
def demo(args):
    # Assert a condition
    assert args.num1 > args.num2

    # Print the results
    print("The difference between", args.num1, "and", args.num2, "is", args.num1 - args.num2)

# Define the parser
parser = argparse.ArgumentParser(description="This program demonstrates assert and argparse.")

# Add arguments to the parser
parser.add_argument("num1", type=int, help="The first number")
parser.add_argument("num2", type=int, help="The second number")

# Parse the arguments
args = parser.parse_args()

# Call the function
demo(args)
