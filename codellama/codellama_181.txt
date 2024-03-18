# Test if a number is even or odd using False and in

def is_even(n):
    return n % 2 == 0

def main():
    num = int(input("Enter a number: "))
    if is_even(num):
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

main()