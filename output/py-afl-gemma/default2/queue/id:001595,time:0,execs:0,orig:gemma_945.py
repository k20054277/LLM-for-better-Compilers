
import tensorflow as tf

# Define a simple linear regression model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Generate sample data
x_train = tf.constant([[1], [2], [3], dtype='int64')
y_train = tf.constant([10, 20, 30], dtype='int64')

# Train the model
model.fit(x_train, y_train, epochs=100)

# Evaluate the model
model.evaluate(x_train, y_train)
