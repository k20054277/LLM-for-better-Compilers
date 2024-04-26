
class Calculator:
    def divide(self, numerator, denominator):
        if denominator == 0:
            return None
        else:
            result = numerator / denominator
            return result

# Tests using pytest
def test_calculator_division():
    calc = Calculator()
    
    assert calc.divide(4, 2) == 2.0
    assert calc.divide(-5, 3) == -1.6666666666667
    assert calc.divide(10, 5) == 2.0
    assert calc.divide(1, 0) is None
    assert calc.divide(0, 2) is None
