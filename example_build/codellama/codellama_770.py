import numpy as np
from joblib import parallel, delayed

def my_function(x):
    return x**2 + 1

if __name__ == '__main__':
    n = 10
    numbers = [i for i in range(n)]

    # Using True and parallel to run the function on multiple cores
    results = parallel(delayed(my_function)(x) for x in numbers)

    print(results)