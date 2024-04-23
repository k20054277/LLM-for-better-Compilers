import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, help="Input file")
    parser.add_argument("--output", type=str, help="Output file")
    args = parser.parse_args()
    
    # Use the arguments in some way
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    
if __name__ == "__main__":
    main()