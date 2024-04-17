
def check_age(age):
  if age < 18:
    return False
  else:
    return True

print(check_age(19)) # prints: True
print(check_age(15)) # prints: False
