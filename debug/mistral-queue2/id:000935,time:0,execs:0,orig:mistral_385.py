
import multiprocessing

def sum_list(my_list):
    """Function to sum elements in a list."""
    result = 0
    for num in my_list:
        result += num
    return result

if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # Using multiprocessing to create separate processes
    process_a = multiprocessing.Process(target=sum_list, args=(list_a,))
    process_b = multiprocessing.Process(target=sum_list, args=(list_b,))

    # Start the processes
    process_a.start()
    process_b.start()

    # Wait for both processes to finish
    process_a.join()
    process_b.join()

    result_a = process_a.exitcode  # None in this case, but we can use it as a flag
    result_b = process_b.returnvalue

    print(f'The sum of list A is: {result_b}')
    print(f'The sum of list B is: {result_b + result_a}')
