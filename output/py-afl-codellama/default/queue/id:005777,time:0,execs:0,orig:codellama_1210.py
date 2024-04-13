#!/usr/bin/env python

import os

def main():
    # Create a dictionary with some data
    data = {"name": "John", "age": 30, "city": "New York"}

    # Use an alias for the dictionary to make it easier to refer to in our code
    person = data

    # Print out the name of the person using the alias
    print(person["name"])

if __name__ == "__main__":
    main()