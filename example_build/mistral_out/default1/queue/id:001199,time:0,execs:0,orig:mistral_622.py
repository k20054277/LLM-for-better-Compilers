
import numpy as np
import tensorflow as tf

# Generate some random data for demonstration purposes.
np.random.seed(42)
x = np.random.randn(100, 3) * 5
y = np.round(np.random.randn(100, 1) + 2).astype('int8')

# Create a boolean mask from the first 50 samples
mask = np.zeros((x.shape[0],), dtype=bool)
mask[:50] = True

# Build and prepare the TensorFlow dataset.
ds = tf.data.Dataset.from_tensor_slices((x, y)).shuffle(buffer_size=len(x))
ds = ds.batch(32).prefetch(tf.data.AUTOTUNE_BUFFER_SIZE)

# Define and build the neural network model.
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossent', metrics=['accuracy'])

# Train the model using the TensorFlow dataset.
epochs = 10
history = model.fit(ds, epochs=epochs, verbose=0)

# Use the mask to evaluate the model performance on the first 50 samples (`True` values).
x_masked = x[mask]
y_masked = y[mask]
loss, accuracy = model.evaluate(tf.data.Dataset.from_tensor_slices((x_masked, y_masked)), verbose=0)
print(f"Model performance on the first 50 samples: loss={loss}, accuracy={accuracy}")
