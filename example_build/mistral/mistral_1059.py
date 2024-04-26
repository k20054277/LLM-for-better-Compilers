
class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def divison(x, y):
    try:
        result = x / y
    except ZeroDivisionError as zero_error:
        raise CustomException("Division by zero is not allowed") from zero_error
    
    return result

try:
    a = int('foo')
    b = 0
    c = divison(a, b)
except CustomException as e:
    print("Error:", e.message)
else:
    print("Result: {:.2f}".format(c))
