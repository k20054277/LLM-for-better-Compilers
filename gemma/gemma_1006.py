
# Import the necessary libraries
import pandas as pd

# Create a sample dataframe
data = pd.DataFrame({"Name": ["John Doe", "Jane Doe", "Peter Pan"], "Age": [25, 30, 12], "City": ["New York", "Los Angeles", "Neverland"]})

# Print the dataframe
print(data)

# Filter the dataframe based on the condition and deploy the results
filtered_data = data[(data["Age"] > 20) & (data["City"] == "New York")]

# Print the filtered dataframe
print(filtered_data)
