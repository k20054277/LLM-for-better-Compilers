
def is_valid_input(input):
    is_number = True
    try:
        num = float(input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        is_number = False
     finally:
        return is_number

while True:
    user_input = input("Enter a number or type 'q' to quit: ")
    if user_input.lower() == 'q':
        break

    is_valid = is_valid_input(user_input)

    if not is_valid:
        continue

    print(f"You entered the number: {user_input}")
