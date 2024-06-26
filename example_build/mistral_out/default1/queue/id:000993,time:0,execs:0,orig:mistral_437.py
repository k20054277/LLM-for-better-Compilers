
# Function with a dependency
def calculate_square_root(number):
    if number < 0:
        print("Error: Negative numbers don't have real square roots")
        return None
    import math
    result = math.sqrt(number)
    return result

# Function with dependency on calculate_square_root
def find_distance(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    sqrt_dx = calculate_square_root(dx)
    sqrt_dy = calculate_square_root(dy)

    distance = sqrt_dx + sqrt_dy

    return distance

if __name__ == "__main__":
    print("Find the distance between (2, 3) and (6, 8)")
    x1, y1 = 2, 3
    x2, y2 = 6, 8

    result = find_distance(x1, y1, x2, y2)

    if result is not None:
        print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {result}")
    else:
        print("Error occurred while calculating the square roots")
