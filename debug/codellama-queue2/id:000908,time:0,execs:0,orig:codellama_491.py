import argparse

# create an argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument("--input", help="the input file")
parser.add_argument("--output", help="the output file")

# parse the arguments from the command line
args = parser.parse_args()

# check if the input and output files were specified
if args.input is None or args.output is None:
    print("Please specify both an input and output file!")
    exit(1)

# do something with the input and output files
with open(args.input, "r") as f_in:
    data = f_in.read()

with open(args.output, "w") as f_out:
    f_out.write(data)