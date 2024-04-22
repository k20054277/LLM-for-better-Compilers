
import tensorflow as tf
import tensorflow_datasets as tfds

# Load XOR dataset
(x_train, y_train), _ = tfds.loads_dataset('xor', with_info=False, split='train')

# Define input shape
input_shape = x_train.shape[1:]

# Create TensorFlow placeholders for the input and output tensors
x = tf.placeholder(tf.float32, shape=[None] + input_shape)
y = tf.placeholder(tf.int8, shape=[None])

# Define weights and biases as variables using tf.Variable
w = tf.Variable(tf.zeros([input_shape[0], 1]))
b = tf.Variable(tf.zeros([1]))

# Define the sigmoid activation function
sigmoid = tf.sigmoid

# Multiply inputs with weights and add bias, then apply activation function
logits = tf.matmul(x, w) + b
predictions = tf.cast(sigmoid(logits) > 0.5, tf.int8)

# Define loss function (binary crossentropy)
loss = tf.reduce_mean(tf.nn.ncelloss(labels=y, predictions=predictions))

# Define optimizer and training steps per epoch
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.5)
train_step = optimizer.minimize(loss)

# Initialize variables and start the TensorFlow graph session
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Training the model for 1000 steps (epochs)
for epoch in range(1, 1001):
    if epoch % 100 == 0:
        print('Epoch {}:'.format(epoch))

    _, loss_val = sess.run([train_step, loss], feed_dict={x: x_train, y: y_train})
    print('Loss: {:.4f}'.format(loss_val))

# Evaluate the trained model on XOR test data
x_test, _ = tfds.loads_dataset('xor', with_info=False, split='test')
test_x = x_test[:10]
test_y = y_train[10:]

_, predictions_val = sess.run([predictions], feed_dict={x: test_x})
print('Test predictions: {}\nTest labels: {}'.format(predictions_val, test_y))

# Close the session
sess.close()
