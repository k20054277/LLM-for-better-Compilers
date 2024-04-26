def main():
    # Demonstrate the use of False and divmod
    a = 10
    b = 3
    c = False

    print(divmod(a, b))  # (3, 1)
    print(divmod(b, a))  # (1, 2)
    print(divmod(a, c))  # (10, 0)

if __name__ == "__main__":
    main()