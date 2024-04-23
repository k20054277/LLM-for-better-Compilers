class MyClass:
    @classmethod
    def my_async(cls):
        print("Hello from MyClass!")

# This will call the method "my_async" on the class "MyClass" asynchronously,
# meaning that it will run in parallel with other code
asyncio.create_task(MyClass.my_async())