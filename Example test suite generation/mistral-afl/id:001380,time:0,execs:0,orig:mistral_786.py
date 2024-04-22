
# Boolean values: True and False
bool_value_1 = True
bool_value_2 = False

print("Boolean value 1 is:", bool_value_1)
print("Boolean value 2 is:", bool_value_2)

# Boolean operators: AND (and), OR (or), and NOT (not)
def boolean_expression():
    condition_1 = True
    condition_2 = False

    # AND operator: Both conditions must be true
    result_and = condition_1 and condition_2
    print("Result of 'condition_1 and condition_2':", result_and)

    # OR operator: At least one condition must be true
    result_or = condition_1 or condition_2
    print("Result of 'condition_1 or condition_2':", result_or)

    # NOT operator: Negates the given boolean value
    result_not = not bool_value_1
    print("Result of 'not bool_value_1' is:", result_not)

boolean_expression()
