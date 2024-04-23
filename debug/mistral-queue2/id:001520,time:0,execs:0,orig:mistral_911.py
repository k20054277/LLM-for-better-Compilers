
import numpy as np
import tensorflow as tf

# Logical operation using NumPy
np_arr1 = np.array([1, 0, 1, 1], dtype=np.float32)
np_arr2 = np.array([1, 1, 0, 1], dtype=np.float32)
and_np = np.logical_and(np_arr1, np_arr2)
print("Logical AND using NumPy:")
print(np_arr1)
print(np_arr2)
print(and_np)

# Building a simple neural network using TensorFlow
input_shape = (1, 4)
x = tf.keras.Input(shape=input_shape, name='input')
x = tf.keras.layers.Dense(32, activation='relu')(x)
y = tf.keras.layers.Dense(1, activation='sigmoid')(x)
model = tf.keras.Model(inputs=x, outputs=y)

# Logical operation using TensorFlow
@tf.function
def logical_and(arr1, arr2):
    return tf.logical_and(arr1, arr2)

np_arr1_tensor = tf.convert_numpy_to_tensor(np_arr1)
np_arr2_tensor = tf.convert_numpy_to_tensor(np_arr2)
result_tf = logical_and(np_arr1_tensor, np_arr2_tensor)
print("\nLogical AND using TensorFlow:")
print("np_arr1_tensor:", np_arr1_tensor.numpy())
print("np_arr2_tensor:", np_arr2_tensor.numpy())
print("result_tf:", result_tf.numpy())

# Compile and train the neural network
model.compile(optimizer='adam', loss='binary_crossent')
model.fit(np.expand_dims(np_arr1, axis=0), np.expand_dims(np_arr2, axis=0), epochs=50)
