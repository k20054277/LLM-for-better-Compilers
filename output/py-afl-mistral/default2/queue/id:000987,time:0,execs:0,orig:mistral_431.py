
def add_numbers(a, b):
    if isinstance(a, (int, float)):
        result = a
        if isinstance(b, (int, float)):
            result = result + b
            return result
        else:
            print("Error! Second argument must be a number.")
            return None
    else:
        print("Error! First argument must be a number.")
        return None
