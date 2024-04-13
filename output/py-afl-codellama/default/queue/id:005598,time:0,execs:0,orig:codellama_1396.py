# Import the math module for the square root function
import math

def calculate_area(radius):
    """Calculate the area of a circle given its radius"""
    assert radius >= 0, "Radius must be non-negative"
    return math.pi * radius ** 2

def main():
    # Test the calculate_area method with positive and negative values
    print("Testing with positive values:")
    print(calculate_area(5))
    print(calculate_area(-3))

    # Test the calculate_area method with zero value
    try:
        print(calculate_area(0))
    except AssertionError as error:
        print("AssertionError:", error)

if __name__ == "__main__":
    main()