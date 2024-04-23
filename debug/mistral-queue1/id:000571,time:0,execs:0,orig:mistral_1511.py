
# Function that checks if a number is a power of 2
def is_power_of_two(n):
    return (n & (n - 1)) == 0 and n > 0

# Function that shifts bits in a binary number
def left_shift(number, positions):
    assert is_power_of_two(positions), "Number of positions must be a power of 2"
    return number << positions

# Test cases for the functions
if __name__ == "__main__":
    num = 10
    print(f"Original number: {bin(num)}")
    
    # Shift bits to the left by 2 positions (which is a power of 2)
    shifted_number = left_shift(num, 2)
    print(f"Number shifted left by 2 positions: {bin(shifted_number)}")
    
    try:
        # Shift bits to the left by an incorrect number of positions (not a power of 2)
        num_incorrect = left_shift(num, 3)
        print(f"Number shifted left by 3 positions (which is not a power of 2): {bin(num_incorrect)}")
    except AssertionError as e:
        print(e)
