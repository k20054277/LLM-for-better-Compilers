async def my_function():
    try:
        await something()
    except Exception as e:
        # handle the exception
        pass
    else:
        assert something(), "Something went wrong"