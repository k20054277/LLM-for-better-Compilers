def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def main():
    print(is_even(10)) # True
    print(is_even(11)) # False

if __name__ == "__main__":
    main()