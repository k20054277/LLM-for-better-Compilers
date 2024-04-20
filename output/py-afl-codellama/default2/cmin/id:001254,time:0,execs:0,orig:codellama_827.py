def main():
    x = 5
    y = 10
    z = 15

    if x < y and x < z:
        print("x is less than both y and z")
    else:
        print("x is not less than both y and z")

    if x > y and x > z:
        print("x is greater than both y and z")
    else:
        print("x is not greater than both y and z")

    if x == y and x == z:
        print("x is equal to both y and z")
    else:
        print("x is not equal to both y and z")

    if x != y and x != z:
        print("x is different from both y and z")
    else:
        print("x is not different from both y and z")

if __name__ == "__main__":
    main()