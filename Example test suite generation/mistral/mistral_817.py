
def check_age(age):
 """
 This function checks if a given age is valid (above 18)
 """

 # First, we check if the input 'age' is an integer
 if isinstance(age, int):
 # Then, we use the logical AND operator 'and' to check if the age is above 18
 if age > 18:
 return True
 else:
 return False
 else:
 print("Error: The input must be an integer.")
 return None
