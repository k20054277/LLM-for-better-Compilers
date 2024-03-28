def greet(name):
    if name == None:
        return "Hello, World!"
    else:
        return f"Hello, {name}!"

def test_greet():
    assert greet(None) == "Hello, World!"
    assert greet("Alice") == "Hello, Alice!"