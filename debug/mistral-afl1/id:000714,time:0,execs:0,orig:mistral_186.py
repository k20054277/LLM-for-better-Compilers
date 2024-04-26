
# This is a Python script showing the use of False as a boolean value
# and some conditional statements

def main():
  # Boolean values in Python
  is_rainy = False
  has_umbrella = True

  if not is_rainy:
    print("It's not raining today!")
  else:
    print("It's raining today. Better bring an umbrella.")
    
  if not (is_rainy and not has_umbrella):
    print("You don't need an umbrella today.")
  else:
    print("Don't forget your umbrella!")

if __name__ == "__main__":
  main()
