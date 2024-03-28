
import gc

def generate_large_list(n):
    """Returns a list of floating point numbers of size n"""
    return [float(i) for i in range(1, n + 1)]

def square(num):
    """Function to calculate the square of given number"""
    return num * num

if __name__ == "__main__":
    # Create a large list of floating point numbers
    my_list = generate_large_list(100000)
    
    # Perform some operations on the list
    squares = [square(num) for num in my_list]
    
    # Use assert statement to check if the length of squares list is equal to length of my_list
    assert len(my_list) == len(squares), "Error: Size of my_list and squares are not same"
    
    # Force garbage collection using gc() function
    gc.collect()
    
    print("List 'my_list' is no longer referenced and can be safely collected by GC.")
