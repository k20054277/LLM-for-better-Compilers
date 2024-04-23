
import tensorflow as tf

# Create a simple tensor
x = tf.constant([[1, 2, 3], [4, 5, 6]])

# Print the tensor
print(x)

# Transpose the tensor
x_t = tf.transpose(x)

# Print the transposed tensor
print(x_t)

# Add the transposed tensor to the original tensor
x_plus_t = x + x_t

# Print the resulting tensor
print(x_plus_t)
