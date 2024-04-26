import pandas as pd
from sklearn.cluster import KMeans

# Load the data
df = pd.read_csv("data.csv")

# Perform clustering using KMeans algorithm
kmeans = KMeans(n_clusters=3)
kmeans.fit(df)

# Print the cluster labels for each row in the dataset
print(kmeans.labels_)