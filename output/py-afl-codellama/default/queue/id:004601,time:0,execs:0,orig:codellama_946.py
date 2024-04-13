def check_and_indent(my_list):
    if len(my_list) > 0:
        print("The list is not empty.")
        for item in my_list:
            print(item)
    else:
        print("The list is empty.")