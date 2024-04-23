
import cProfile

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Profile the factorial function
cProfile.run('factorial(5)', 'factorial.prof')

# Analyze the profile
with open('factorial.prof') as f:
    print(f.read())
