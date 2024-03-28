
# Define a function that checks if a number is even or odd using a flag variable 'is_even'
def check_even_odd(num):
    is_even = False  # Initially assume the number is odd
    
    # Check if the number is even or odd based on its remainder when divided by 2
    if num % 2 == 0:
        is_even = True
        
    return is_even, num

# Use the function to check for a few numbers and print the results
for i in range(5):
    even_odd = check_even_odd(i)
    print(f"{i} is {'' if even_odd[0] else 'odd'} and its square is {i**2}")
