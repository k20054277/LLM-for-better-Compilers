
def check_number(numbers):
    for num in numbers:
        if num is None:
            print("Skip '{}' as it is None".format(str(num)))
            continue
        
        if num % 2 == 0:
            print("Even number: {}".format(num))
        else:
            print("Odd number: {}".format(num))
            
# List of numbers and a None value
numbers = [1, 2, 3, 4, 5, None]
check_number(numbers)
