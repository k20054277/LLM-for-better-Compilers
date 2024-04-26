import tensorflow as tf

# Create a constant tensor containing the value 5
constant = tf.constant(5)

# Create a variable tensor containing the value 10
variable = tf.Variable(10)

# Create a placeholder tensor to be filled with a value at runtime
placeholder = tf.placeholder(tf.float32, shape=())

# Use the `True` keyword to create a boolean tensor that is always true
true_tensor = tf.constant(True)

# Use the `False` keyword to create a boolean tensor that is always false
false_tensor = tf.constant(False)

# Use the `tf.equal()` function to compare the value of the constant and variable tensors
result = tf.equal(constant, variable)

# Print the result of the comparison
print(result)

# Use the `tf.equal()` function to compare the value of the constant and placeholder tensors
result2 = tf.equal(constant, placeholder)

# Print the result of the comparison
print(result2)