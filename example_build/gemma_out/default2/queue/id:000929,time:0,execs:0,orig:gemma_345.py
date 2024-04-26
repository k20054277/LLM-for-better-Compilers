
def foo():
  local x = 10
  print(x)  # Output: 10
  print(False)  # Output: False

foo()
print(x)  # Output: NameError: x is not defined
