import multiprocessing

def do_work(n):
    return n * 2

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        result = pool.map(do_work, [1, 2, 3])

    print(result)