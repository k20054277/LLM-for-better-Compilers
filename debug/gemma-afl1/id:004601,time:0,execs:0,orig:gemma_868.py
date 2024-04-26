
import numpy as np

# Define a complex number
z = 3 + 4j

# Print the real and imaginary parts of z
print("Real part:", z.real)
print("Imaginary part:", z.imag)

# Print the magnitude and phase of z
print("Magnitude:", np.abs(z))
print("Phase:", np.angle(z))

# Perform operations on z
w = 2*z + 5j

# Print w
print("W:")
print(w)

# Compare z and w
if z == w:
    print("Z and W are equal")
else:
    print("Z and W are not equal")
