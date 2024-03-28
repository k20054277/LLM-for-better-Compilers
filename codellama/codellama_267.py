def is_even(n):
    if n == 0:
        return True
    elif n < 0:
        return False
    else:
        return is_even(n - 1)

print(is_even(-1)) # Should print False
print(is_even(0)) # Should print True
print(is_even(1)) # Should print False
print(is_even(2)) # Should print True