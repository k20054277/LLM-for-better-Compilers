
# Slicing in Python

def main():
    # Define a list
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Slice the list from index 2 to 5 (inclusive)
    slice1 = numbers[2:5]
    print(f"Slice 1: {slice1}")

    # Slice the list from index -2 to the end (-1 means the last index)
    slice2 = numbers[-2:]
    print(f"Slice 2: {slice2}")

if __name__ == "__main__":
    main()
