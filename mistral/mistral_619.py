
# Import required libraries
import pandas as pd

# Create a sample data as a dictionary
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami']
}

# Create a DataFrame from the data dictionary using pandas
df = pd.DataFrame(data)

# Filter the DataFrame based on Age > 30 using a boolean condition (True)
filtered_df = df[df['Age'] > 30]

# Display the filtered DataFrame
print(filtered_df)
