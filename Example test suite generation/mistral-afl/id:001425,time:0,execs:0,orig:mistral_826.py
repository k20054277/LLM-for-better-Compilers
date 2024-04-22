
def count_bits(num):
    """Return the number of bits set to 1 in the given integer."""
    return sum([int(bit) for bit in bin(abs(num))[2:].zfill(8)[::-1]])

def has_three_bits_set(x, y):
    """Check if two numbers have exactly three bits set to 1."""
    return count_bits(x) == 3 and count_bits(y) == 3 and x != y

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if has_three_bits_set(num1, num2):
        print(f"Both numbers have exactly three bits set to 1.")
        print(f"Binary representation of {num1}: {bin(num1)[2:]}")
        print(f"Binary representation of {num2}: {bin(num2)[2:]}")
    else:
        print("The numbers do not meet the criteria.")
