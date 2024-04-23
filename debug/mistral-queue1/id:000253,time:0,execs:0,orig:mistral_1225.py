
# Simple Python script using 'as' keyword for variable assignment
import numpy as np

x = np.random.rand(5)
y = np.random.rand(5)

z = np.dot(x, y)

sum_of_squares = np.sum(np.square(x))
mean_of_x = np.mean(x)

print(" z = {}".format(z))
print(" sum of squares = {}".format(sum_of_squares))
print(" mean of x = {}".format(mean_of_x))
