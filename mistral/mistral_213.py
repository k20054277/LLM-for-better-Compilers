
import gc
import sys

def func():
    # Create a large list and assign it to 'big_list' variable
    big_list = [i for i in range(10000)]
    
    # Assign an unnecessary variable 'unused' which will refer to False
    unused = False
    
    print("Before collection")
    print("Big List : ", id(big_list))
    print("Unused Variable: ", id(unused))
    
    # Manually trigger the garbage collector using gc.collect()
    gc.collect()
    
    print("\nAfter collection")
    print("Big List : ", id(big_list))
    print("Unused Variable: ", id(unused))

func()
