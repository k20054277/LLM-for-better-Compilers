
import tensorflow as tf

def add_numbers(x, y):
    """Adds two given numbers."""
    result = x + y
    assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Both numbers must be either int or float."
    assert result is not None, f"Error: The sum of {x} and {y} is not defined."
    return result

def add_two_numbers_using_tensorflow(x, y):
    """Adds two given numbers using TensorFlow."""
    x_tensor = tf.constant(x)
    y_tensor = tf.constant(y)
    sum = tf.add(x_tensor, y_tensor)
    result = sum.numpy()
    assert not tf.is_nan(sum), "Error: The sum of {x} and {y} contains NaN values."
    return result

if __name__ == "__main__":
    num1 = 5.0
    num2 = 3.0

    print("Adding numbers using Python's built-in assert statement:")
    result_python = add_numbers(num1, num2)
    assert result_python == num1 + num2, "Error: add_numbers function is not working as expected."

    print("\nAdding numbers using TensorFlow's assert statement:")
    result_tensorflow = add_two_numbers_using_tensorflow(num1, num2)
    tf.assert_equal(result_tensorflow, num1 + num2)
