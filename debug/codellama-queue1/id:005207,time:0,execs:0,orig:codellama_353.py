# Import the necessary libraries
import numpy as np
from scipy.stats import binom

# Define a random variable X with a Bernoulli distribution
X = np.random.binomial(n=1, p=0.5)

# Evaluate the probability of X being 0 or 1
p_x = binom.pmf(k=X, n=1, p=0.5)
print("Probability of X being 0 or 1:", p_x)

# Use conda to install a new package
conda install -c anaconda seaborn