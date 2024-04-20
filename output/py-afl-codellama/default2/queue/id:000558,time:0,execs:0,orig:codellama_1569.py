class MyClass:
    @staticmethod
    def my_static_method(x, y):
        return x + y

    @async
    async def my_async_method(self, x, y):
        result = await self.my_static_method(x, y)
        return result * 2

instance = MyClass()
result = instance.my_async_method(1, 2).result()
print(result)