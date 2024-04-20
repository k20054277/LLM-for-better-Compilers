import tensorflow as tf

# Create a tensor with values 0, 1, and 2
x = tf.constant([0, 1, 2])

# Create a tensor with values 3, 4, and 5
y = tf.constant([3, 4, 5])

# Use the `and` operator to compute the intersection of x and y
z = tf.boolean_mask(x, tf.logical_and(x, y))

# Print the result
print(z)