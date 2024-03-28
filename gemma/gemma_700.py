
import argparse

# Define a parser
parser = argparse.ArgumentParser()

# Add arguments to the parser
parser.add_argument("command", help="The command to be executed")
parser.add_argument("argument", help="The argument for the command")

# Parse the arguments
args = parser.parse_args()

# Print the arguments
print("Command:", args.command)
print("Argument:", args.argument)

# Check if the command is true
if args.command is True:
    print("The command is True")
else:
    print("The command is not True")
