import threading

def check_primes(numbers):
    for number in numbers:
        if number < 2:
            continue
        for i in range(2, number):
            assert number % i != 0, f"{number} is not a prime number."

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threading.Thread(target=check_primes, args=(numbers,)).start()