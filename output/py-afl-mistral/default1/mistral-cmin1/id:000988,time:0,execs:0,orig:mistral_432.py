
# Function to calculate the square root of a number (with and without optimization)
def sqrt_none(number):
    if number < 0:
        return None  # If number is negative, return None
    else:
        import math
        return math.sqrt(number)

# Function to calculate the square root of a number with caching optimization
cache = {}

def sqrt_cache(number):
    if number < 0:
        return None  # If number is negative, return None
    elif number in cache:
        return cache[number]
    else:
        result = math.sqrt(number)
        cache[number] = result
        return result

if __name__ == "__main__":
    numbers = [25.0, 4.0, -1.0, 36.0, 16.0]
    for number in numbers:
        print(f"Square root of {number} is:")
        square_root = sqrt_none(number)
        if square_root is not None:
            print(square_root)
        else:
            print("Error: negative number detected.")

        square_root = sqrt_cache(number)
        if square_root is None:
            print("Error: negative number detected in cache function too.")
        else:
            print(f"Cached result: {square_root}")
