import os

def main():
    # Assert that the file exists
    assert os.path.exists("example_file.txt")

    # Shell command to delete the file
    os.system("rm example_file.txt")

if __name__ == "__main__":
    main()