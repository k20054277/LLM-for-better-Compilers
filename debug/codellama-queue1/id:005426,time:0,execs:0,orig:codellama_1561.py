# This program demonstrates the use of async and repr

async def foo(x):
    return x * 2

repr_result = repr(foo)
print(repr_result)

result = await foo(5)
print(result)