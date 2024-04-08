def get_unique_id(name):
    assert len(name) > 0, "Name cannot be empty"
    return hash(name) % (10 ** 8)

# Test the function with some inputs
print(get_unique_id("Alice"))
print(get_unique_id("Bob"))
print(get_unique_id("Charlie"))