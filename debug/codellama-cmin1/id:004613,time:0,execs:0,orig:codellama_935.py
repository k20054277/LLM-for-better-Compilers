def iter_and(my_list):
    result = []
    for i in my_list:
        if i % 2 == 0:
            result.append(i)
    return result

print(iter_and([1, 2, 3, 4, 5])) # Output: [2, 4]