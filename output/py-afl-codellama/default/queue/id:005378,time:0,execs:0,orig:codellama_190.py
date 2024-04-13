with open("example.txt", "w") as file:
    if not file.write("Hello, world!"):
        print("Failed to write to file")
    else:
        print("Successfully wrote to file")

# Output: Successfully wrote to file