from joblib import Parallel, delayed
import time

def my_function(x):
    # do some computation
    return x**2

if __name__ == '__main__':
    # create a list of inputs for the function
    inputs = [1, 2, 3, 4, 5]
    
    # use `as` to give each input a unique name
    results = Parallel(n_jobs=2)(delayed(my_function)(x) for x in inputs)
    
    print(results)