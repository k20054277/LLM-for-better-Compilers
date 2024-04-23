
def check_age(age):
 """
 This function checks if a given age is valid (above 18) and returns the status as a boolean value or "Adult" string.
 """
 is_valid_age = age > 18
 if is_valid_age:
 return "Adult"
 else:
 return False
