
# Define two Boolean variables
bool_var1 = True
bool_var2 = False

# Demonstrate the usage of False
print("Boolean variable 1: ", bool_var1)
print("Negation of boolean variable 1 using not keyword: ", not bool_var1)
print("Comparison between two boolean variables: ", bool_var1 and bool_var2)
print("Output when using an if statement with False as condition:")
if False:
    print("This statement will not be executed.")

# Demonstrate the usage of bitwise XOR (^) operator
int_var1 = 5 # binary: 0101
int_var2 = 3 # binary: 0011

print("\nInteger variables:")
print("Variable 1: ", int_var1)
print("Variable 2: ", int_var2)

xor_result = int_var1 ^ int_var2
print("Result of XOR operation:")
print(bin(int_var1)[2:].zfill(8), "^", bin(int_var2)[2:].zfill(8), "=", bin(xor_result)[2:].zfill(8))
print("Decimal representation of the XOR result: ", xor_result)
