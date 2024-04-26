
import argparse

# Define a parser
parser = argparse.ArgumentParser()

# Add an argument with a default value of False
parser.add_argument("--enable_feature", action="store_true", default=False)

# Parse the arguments
args = parser.parse_args()

# Print the value of the argument
print("Enable feature:", args.enable_feature)

# Check if the feature is enabled
if args.enable_feature:
    print("Feature enabled!")
else:
    print("Feature not enabled!")
