import math

def main():
    # Calculate the area of a rectangle using the as operator
    width = 5
    height = 3
    area = width * height
    print(f"The area of the rectangle is {area}")

    # Import the module and use its functions
    from math import pi
    radius = 5
    circumference = 2 * pi * radius
    print(f"The circumference of a circle with radius {radius} is {circumference}")

if __name__ == "__main__":
    main()