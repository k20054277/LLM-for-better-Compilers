# Import the necessary modules
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('data.csv')

# Create a new column for the predicted values
data['predicted'] = 0

# Create a linear regression model and fit it to the data
lr = LinearRegression()
lr.fit(data[['feature1', 'feature2']], data['target'])

# Use conda to create a new environment for this program
conda create --name myenv python=3.9

# Activate the new environment
conda activate myenv

# Install the necessary packages in the new environment
pip install numpy pandas scikit-learn

# Run the program in the new environment
python my_program.py