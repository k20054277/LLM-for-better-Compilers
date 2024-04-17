
# This program finds the first occurrence of an even number in a given list
# Using nested for loop and break keyword

def find_even_number(numbers):
    for i, num in enumerate(numbers):
        for j in range(2, num+1):
            if num % j == 0:
                print(f'The number {num} is not an even number')
                break
        else:
            print(f'The number {num} is an even number. Exiting the loop.')
            return numbers[i]
    print("No even number found in the given list.")

if __name__ == "__main__":
    numbers = [1, 3, 5, 6, 8, 9, 12]
    result = find_even_number(numbers)
    if result is not None:
        print(f'The first even number found in the list is {result}.')
