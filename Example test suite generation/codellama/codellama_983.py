import os

def print_memory_usage():
    print(f"Memory usage: {os.memory_usage().rss}")

def demonstrate_and_memory_management():
    # create a list of 100 numbers
    numbers = [i for i in range(100)]

    # print the initial memory usage
    print_memory_usage()

    # create a set of the numbers and remove duplicates
    unique_numbers = set(numbers)

    # print the memory usage after creating the set
    print_memory_usage()

    # create a list of 100 strings
    strings = [str(i) for i in range(100)]

    # print the memory usage after creating the list of strings
    print_memory_usage()

    # remove elements from the set that are not in the list
    unique_numbers.intersection_update(strings)

    # print the memory usage after removing elements from the set
    print_memory_usage()

# demonstrate the use of and and memory management
demonstrate_and_memory_management()