
import cProfile

def function(x):
    if x is None:
        return None
    else:
        return x ** 2

# Profiling the function
cProfile.run('function(None)', 'profile.txt')

# Analyzing the profile
with open('profile.txt') as f:
    print(f.read())
