
def function_with_as_and_finally():
    try:
        print("Inside try block")
        with open("file.txt") as f:
            print("File content:", f.read())
    finally:
        print("Inside finally block")

function_with_as_and_finally()
