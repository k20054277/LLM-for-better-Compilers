#!/usr/bin/env python3

try:
    x = int(input("Enter a number: "))
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
except ValueError:
    print("Invalid input. Please enter an integer.")