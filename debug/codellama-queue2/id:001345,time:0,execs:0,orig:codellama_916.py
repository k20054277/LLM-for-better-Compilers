import tensorflow as tf

# Define two tensors
a = tf.constant([1, 2, 3])
b = tf.constant([4, 5, 6])

# Use `and` to compute the element-wise logical AND of the two tensors
c = a & b

print(c) # Output: [True True False]