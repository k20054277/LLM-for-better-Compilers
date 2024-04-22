
def modify_number(num):
    # Calculate remainder of num % 2
    remainder = num % 2

    # Set is_even to True if num is even (remainder is 0)
    is_even = True if remainder == 0 else False

    print("Number: {num} | Remainder: {remainder} | Is Even: {is_even}")

# Test the function with some numbers
modify_number(4)
modify_number(5)
modify_number(12)
