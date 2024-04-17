my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = list(filter(lambda x: x > 5 and x % 2 == 0, my_list))
print(filtered_list)