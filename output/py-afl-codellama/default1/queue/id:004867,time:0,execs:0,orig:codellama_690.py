import sys

def my_function():
    print("Hello World")

if __name__ == "__main__":
    if sys.argv[1].lower() == "true":
        my_function()