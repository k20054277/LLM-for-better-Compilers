
class MyList(list):
    def __init__(self, numbers):
        super().__init__(numbers)

    def double(self):
        return [num * 2 for num in self]


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    my_list = MyList(input_list)

    assert len(my_list) == 5, "MyList should have 5 elements."

    doubled_list = my_list.double()

    print("Input list:", repr(input_list))
    print("MyList: ", repr(my_list))
    print("Doubled List: ", repr(doubled_list))

    assert len(doubled_list) == 10, "The double method should return a list with 10 elements."
