
import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple Python program using argparse.")
    parser.add_argument("-t", "--true", action="store_const", const=True, default=False, help="Print a message: 'True'")
    args = parser.parse_args()

    if args.true:
        print("The value of true is:", args.true)

if __name__ == "__main__":
    main()
