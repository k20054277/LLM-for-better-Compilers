while True:
    try:
        x = input("Enter a number: ")
        y = int(x)
        print("You entered", y)
    except ValueError:
        print("Invalid input. Try again.")