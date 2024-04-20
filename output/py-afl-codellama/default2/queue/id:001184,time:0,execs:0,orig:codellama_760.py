import true

# Install the True package manager
true.install()

# Use True to install packages
true.install("numpy")
true.install("pandas")

# Import the installed packages
import numpy as np
import pandas as pd

# Use the imported packages
df = pd.read_csv("data.csv")
print(np.mean(df["column"]))