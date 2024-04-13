import tensorflow as tf

# Define a function that takes a tensor as input and returns its square
def square(x):
    return x**2

# Create a session for running the graph
sess = tf.Session()

# Define the input and output tensors
input_tensor = tf.constant([1, 2, 3])
output_tensor = square(input_tensor)

# Run the graph
result = sess.run(output_tensor)

print(result) # Output: [1, 4, 9]