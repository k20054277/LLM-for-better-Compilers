with open("file.txt", "r") as file:
    try:
        assert file.read() == "hello"
    except AssertionError:
        print("Failed to read 'hello' from file.")