
import concurrent.futures
import time

def func(x):
    """Function to be applied to each input."""
    print(f'Function {x} started at {time.ctime()}.')
    time.sleep(2)
    print(f'Function {x} finished at {time.ctime()}.')
    return x > 3

if __name__ == '__main__':
    inputs = [1, 2, 3, 4]

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(inputs)) as executor:
        futures = {executor.submit(func, i): i for i in inputs}
        results = {future.result() for future in concurrent.futures.as_completed(futures)}

    print('\nResults:')
    for input_, result in results.items():
        print(f'Input: {input_}, Result: {result}')

    and_result = all(results.values())  # Logical AND of all results
    print(f'\nLogical AND ({", ".join(str(i) for i in inputs)}): {and_result}')
