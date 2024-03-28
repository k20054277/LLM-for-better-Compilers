
def hello(name):
  """Says hello to a person."""
  return "Hello, " + name

assert hello("John") == "Hello, John"
assert hello("Jane") == "Hello, Jane"

print(hello("Bob"))
