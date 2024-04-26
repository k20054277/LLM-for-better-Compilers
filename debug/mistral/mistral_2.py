
# A simple function that checks if a given number is positive, zero or negative.
def check_number(num):
    # If the number is less than 0, then it is negative.
    if num < 0:
        return False, num
    
    # If the number is equal to 0, it is a special case and we use None for this.
    elif num == 0:
        return None, "Zero"
    
    # Otherwise, the number is positive.
    else:
        return True, num

# Test the function with some numbers.
num = 5
is_positive, number = check_number(num)
print(f'The number {number} is positive: {is_positive}')

num = -3
is_positive, number = check_number(num)
print(f'The number {number} is positive: {is_positive}')

num = 0
is_positive, number = check_number(num)
if is_positive is None:
    print(f"The number {number} is zero.")
else:
    print(f'The number {number} is positive: {is_positive}')
