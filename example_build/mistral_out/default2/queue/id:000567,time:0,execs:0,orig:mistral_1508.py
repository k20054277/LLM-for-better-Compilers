
# Define a function with an assertion
def add_and_check(x, y):
    result = x + y
    
    # Assert statement to check if two numbers are positive
    assert x > 0 and y > 0, "Both numbers must be positive"
    
    # Bitwise OR operation (|) to set a variable to the binary representation of a number
    binary_x = Bin(x).to_bin()
    binary_y = Bin(y).to_bin()
    sum_bits = binary_x | binary_y
    
    # Convert binary representation back to decimal and store in a new variable
    assert abs(int(sum_bits, 2)) == result, "Bitwise OR operation does not equal addition result"
    
    return result

# Define a custom Bin class for converting integers to binary
class Bin:
    @staticmethod
    def to_bin(num):
        return format(abs(num), base=2)

if __name__ == "__main__":
    add_and_check(3, 4)
    add_and_check(-3, 4)
