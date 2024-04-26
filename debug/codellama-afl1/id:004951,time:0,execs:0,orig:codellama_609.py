import asyncio

async def foo():
    # This function returns a boolean value indicating whether it was successful or not
    return True

async def bar():
    # This function returns the result of calling foo()
    return await foo()

# Calling bar() will run the coroutine foo() and print "True" if it was successful
print(await bar())