import tensorflow as tf
from PIL import Image
import numpy as np

# Load the model using TensorFlow's SavedModel format
model = tf.keras.models.load_model('path/to/saved/model')

# Load an image using PIL and convert it to a NumPy array
img = Image.open('path/to/image.jpg')
img_array = np.array(img)

# Preprocess the image by resizing and normalizing the pixel values
img_array = tf.image.resize(img_array, (224, 224))
img_array = img_array / 127.5 - 1

# Predict the class of the image using the pretrained model
prediction = model.predict(np.expand_dims(img_array, axis=0))[0]

# Print the predicted class and confidence score
print('Predicted class: {}, Confidence: {}'.format(prediction['class'], prediction['score']))