import multiprocessing

def my_function(x):
    return x * x

if __name__ == '__main__':
    inputs = [1, 2, 3, 4, 5]
    with multiprocessing.Pool() as p:
        results = p.map(my_function, inputs)
        print(results)