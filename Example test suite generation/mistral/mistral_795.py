
# A simple program to find the first occurrence of an even number in a given list using 'and' operator and 'break' statement

def find_even_number(numbers):
    for i, num in enumerate(numbers):
        if num % 2 == 0:  # check if number is even
            print("First even number found at index:", i)
            break
        if i + 1 == len(numbers):
            print("No even numbers were found.")
            return

if __name__ == "__main__":
    numbers = [1, 3, 5, 6, 8]
    find_even_number(numbers)
