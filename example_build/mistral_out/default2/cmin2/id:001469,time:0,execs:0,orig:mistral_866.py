
class MyClassA:
    def __init__(self, value_a):
        self.value_a = value_a

class MyClassB:
    def __init__(self, value_b):
        self.value_b = value_b

def main():
    obj_a = MyClassA(10)
    obj_b = MyClassB(20)

    # Using and operator with two boolean expressions
    result = (obj_a.value_a > 5) and (obj_b.value_b > 15)

    if result:
        print("Both conditions are true")
    else:
        print("At least one condition is false")

if __name__ == "__main__":
    main()
