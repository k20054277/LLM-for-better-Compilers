
# This function takes no argument and returns None
def my_function():
    print("This function does nothing and returns None")
    return None

# This is the main function where we call my_function()
def main():
    result = my_function()
    if result is None:
        print("Function returned None")
    else:
        print("Function returned something other than None")
        print("Result is:", result)

# Call the main function
if __name__ == "__main__":
    main()
