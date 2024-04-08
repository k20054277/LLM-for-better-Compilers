def demo_false(x):
    if x:
        print("True")
    else:
        print("False")

try:
    demo_false(0)
except ValueError as e:
    print(e)