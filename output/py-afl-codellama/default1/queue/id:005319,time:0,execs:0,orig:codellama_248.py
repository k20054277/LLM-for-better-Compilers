import tensorflow as tf

# Define a tensor with shape (3, 4)
t = tf.constant([[1, 2], [3, 4], [5, 6]])

# Create a session to run the graph
sess = tf.Session()

# Run the graph and get the output
output = sess.run(t)
print(output)

# Set the value of t to False
t = tf.constant(False)

# Run the graph again and get the output
output = sess.run(t)
print(output)