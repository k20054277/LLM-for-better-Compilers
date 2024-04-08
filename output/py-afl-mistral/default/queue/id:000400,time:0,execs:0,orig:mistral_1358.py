
def power_function(base, exponent):
    """
    This function returns the base raised to the given exponent using the built-in pow function
    :param base: base number
    :param exponent: exponent
    :return: base raised to the given exponent
    """
    result = pow(base, exponent)
    return result

def test_power_function():
    """
    This function contains some tests for the power_function using assert statements
    """
    # Test 1: Base is 2 and exponent is 3
    assert power_function(2, 3) == 8

    # Test 2: Base is -2 and exponent is 3
    assert power_function(-2, 3) == -8

    # Test 3: Base is 0 and exponent is any number
    with pytest.raises(ZeroDivisionError):
        power_function(0, 5)
        
if __name__ == "__main__":
    test_power_function()
