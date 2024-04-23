def main():
    # create a list of numbers
    nums = [1, 2, 3, 4, 5]
    
    # use a lambda function to filter out even numbers
    even_nums = list(filter(lambda x: x % 2 == 0, nums))
    
    print("Even numbers:", even_nums)
    
    # use a lambda function to filter out odd numbers
    odd_nums = list(filter(lambda x: x % 2 != 0, nums))
    
    print("Odd numbers:", odd_nums)

if __name__ == "__main__":
    main()