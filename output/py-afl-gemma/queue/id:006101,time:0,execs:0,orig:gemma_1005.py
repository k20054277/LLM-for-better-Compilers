
import cProfile

def my_function(n):
    sum = 0
    for i in range(n):
        sum += i

# Profile the function
cProfile.run('my_function(100000)')

# Print the profile
cProfile.printProfile()
