
# This function checks if a number is positive, even and its second power is greater than 100
def is_special(num):
    if num > 0 and num % 2 == 0 and num ** 2 > 100:
        return True
    else:
        return False

# Test some numbers
for i in range(-5, 6):
    print(f"Number {i} is special: {is_special(i)}")
