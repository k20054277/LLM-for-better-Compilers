def get_number():
    return int(input("Enter a number: "))

while True:
    try:
        num = get_number()
        if num is None:
            raise ValueError("Invalid input")
        print(num)
    except ValueError as e:
        print("Invalid input. Please enter a valid number.")