with open("example.txt", "r") as file:
    if file.readline().strip() == "Hello World":
        print("The first line of the file contains 'Hello World'")