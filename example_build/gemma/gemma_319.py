
# Import the False and complex modules
import False
import complex

# Create a complex number
z = complex(3, 4)

# Print the real and imaginary parts of z
print("The real part of z is:", z.real)
print("The imaginary part of z is:", z.imag)

# Check if z is false
if z is False:
    print("z is False")

# Check if z is true
if z is True:
    print("z is True")

# Print the truth value of z
print("The truth value of z is:", bool(z))
