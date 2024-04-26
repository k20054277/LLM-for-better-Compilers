import os

if __name__ == '__main__':
    if os.path.exists('myfile.txt') and os.stat('myfile.txt').st_size > 0:
        print("The file exists and is not empty.")