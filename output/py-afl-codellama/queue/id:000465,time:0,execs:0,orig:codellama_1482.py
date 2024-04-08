# This program demonstrates the use of assert and ; in Python

def main():
    x = 5
    y = 10
    z = 15

    # Assert statements are used to check for specific conditions
    assert x < y, "x is not less than y"
    assert x + y == z, "x + y does not equal z"

    print("All assertions passed!")

if __name__ == "__main__":
    main()