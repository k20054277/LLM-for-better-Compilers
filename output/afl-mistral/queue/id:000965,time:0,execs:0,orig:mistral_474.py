
# This function checks if a given number is less than or equal to 0, and if not, sets the default value to None
def check_number(num):
    if num <= 0:
        return 0
    else:
        return None

# Test cases
print(check_number(5)) # None
print(check_number(-1)) # 0
print(check_number(3)) # None
