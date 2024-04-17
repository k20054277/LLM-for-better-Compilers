
def main():
    # List of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for i in numbers:
        print(f"Current number is {i}")
        
        if i % 2 == 0:
            # Even number found, let's skip the rest of the inner loop
            print("Found even number! Breaking...")
            break
        
        for j in range(1, i+1):
            if i % j == 0:
                # Found a factor other than 1 and number itself
                print(f"Number {i} has a factor {j}")
                factor_found = True
                break
            
        if not factor_found:
            print(f"Current number {i} is prime.")
            next_prime(i)
        
        factor_found = None

def next_prime(num):
    """Helper function to print the next prime after given number"""
    is_prime = True
    
    for i in range(num + 1, float('inf')):
        if num % i == 0:
            is_prime = False
            break
        
        if not is_prime:
            print(f"Next prime after {num} is {i}")
            return

if __name__ == "__main__":
    main()
