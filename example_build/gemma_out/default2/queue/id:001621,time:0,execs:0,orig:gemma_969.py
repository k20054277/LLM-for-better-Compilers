
def fizz_buzz(n):
  """Returns 'fizz' if n is divisible by 3, 'buzz' if n is divisible by 5,
  and n otherwise.

  Args:
    n: The number to check.

  Returns:
    The string 'fizz', 'buzz', or n.
  """

  if n % 3 == 0 and n % 5 == 0:
    return 'fizzbuzz'
  elif n % 3 == 0:
    return 'fizz'
  elif n % 5 == 0:
    return 'buzz'
  else:
    return str(n)


# Print the fizz-buzz for numbers from 1 to 10
for i in range(1, 11):
  print(fizz_buzz(i))
