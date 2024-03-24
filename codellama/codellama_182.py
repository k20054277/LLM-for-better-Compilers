def demo_false(func):
    return func()

def lambda_function():
    return "Lambda function"

print(demo_false(lambda: lambda_function()))