import argparse

# create an argument parser
parser = argparse.ArgumentParser()

# add arguments to the parser
parser.add_argument("--bool", action="store_true", help="a boolean flag")
parser.add_argument("--str", type=str, help="a string argument")
parser.add_argument("--int", type=int, help="an integer argument")

# parse the arguments
args = parser.parse_args()

# check if the --bool flag was set
if args.bool:
    print("The boolean flag was set to True")

# check if the --str argument was provided
if args.str is not None:
    print(f"The string argument was {args.str}")

# check if the --int argument was provided
if args.int is not None:
    print(f"The integer argument was {args.int}")