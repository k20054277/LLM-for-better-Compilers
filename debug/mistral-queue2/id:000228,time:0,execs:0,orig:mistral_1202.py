
# Example 1: Unpacking a tuple using as
try:
    response = requests.get("http://example.com")
    status_code, content = response.status_code, response.content
except Exception as e:
    print("An error occurred:", e)

# Using 'as' to assign the exception name for better debugging
exception = Exception as e
print("Caught an exception of type:", type(exception))
print("Exception message:", exception.args[0])
