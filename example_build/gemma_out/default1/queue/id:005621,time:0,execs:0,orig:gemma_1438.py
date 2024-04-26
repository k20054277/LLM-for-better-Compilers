
import scikit_learn
from scikit_learn.utils.assert_array_shape import assert_array_shape

# Import the dataset
X_train, X_test, y_train, y_test = scikit_learn.load_dataset('iris')

# Assert the shape of the input data
assert_array_shape(X_train, (50, 4))
assert_array_shape(X_test, (100, 4))

# Assert the shape of the labels
assert_array_shape(y_train, (50,))
assert_array_shape(y_test, (100,))

# Print the results
print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)
