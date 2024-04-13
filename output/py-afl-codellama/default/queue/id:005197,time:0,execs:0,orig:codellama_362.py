from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(f, [1, 2, 3, 4, 5])
    print(results)