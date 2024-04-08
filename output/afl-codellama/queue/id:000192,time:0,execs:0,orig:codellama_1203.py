import pandas as pd
import numpy as np
from scipy import stats

# create some sample data
data = {'x': [1, 2, 3], 'y': [4, 5, 6]}
df = pd.DataFrame(data)

# use conda to install the statsmodels package
conda install -c conda-forge statsmodels

# import the statsmodels package and use it to perform a regression
from statsmodels.regression.linear_model import OLS
result = OLS(df['y'], df['x']).fit()
print(result.summary())